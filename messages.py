from db import db
import users
from sqlalchemy.sql import text


def get_list():
    sql = "SELECT M.title, U.username, M.sent_at, M.description, M.id FROM courses M, users U " \
          "WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(text(sql))
    return result.fetchall()

def get_list_for_menu(user_id):
    sql = "SELECT M.title, U.username, M.sent_at, M.description, M.id FROM courses M, users U " \
          "WHERE M.user_id=U.id AND U.id = (:user_id) ORDER BY M.id"
    result = db.session.execute(text(sql), {"user_id":user_id})
    return result.fetchall()

def read_course_material(idd):
    sql = "SELECT C.textcontent FROM coursecontent C WHERE C.course_id = (:id)"
    result = db.session.execute(text(sql), {"id":idd})
    rivi = result.fetchone()
    if rivi:
        return rivi[0]
    else: return None




def send(content, description,textcontent):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        sql = "INSERT INTO courses (title, user_id, description, sent_at) VALUES (:content, :user_id, :description, NOW()) RETURNING id"

        sql2 = "INSERT INTO coursecontent (course_id, textcontent) VALUES (:course_id, :textcontent)"

        courses_id_get = db.session.execute(text(sql), {"content":content, "user_id":user_id, "description":description}).fetchone()

        if courses_id_get:
            course_id = courses_id_get[0]
        else: return False

        db.session.execute(text(sql2), {"course_id":course_id, "textcontent":textcontent})

        db.session.commit()
        return True
    except:
        return False