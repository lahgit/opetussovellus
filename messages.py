from db import db
import users
from sqlalchemy.sql import text


def get_list():
    sql = "SELECT M.title, U.username, M.sent_at, M.description, M.id FROM courses M, users U " \
          "WHERE M.user_id=U.id ORDER BY M.id"
    result = db.session.execute(text(sql))
    return result.fetchall()

def get_desc(id):
    sql = "SELECT C.description FROM courses C WHERE C.id = (:id)"
    result = db.session.execute(text(sql), {"id":id})
    return result.fetchone()

def get_list_for_menu(user_id):
    sql = "SELECT M.title, U.username, M.sent_at, M.description, M.id FROM courses M, users U " \
          "WHERE M.user_id=U.id AND U.id = (:user_id) ORDER BY M.id"
    result = db.session.execute(text(sql), {"user_id":user_id})
    return result.fetchall()

def get_course(course_id):
    sql = "SELECT M.title, U.username, M.sent_at, M.description, M.id FROM courses M, users U " \
          "WHERE M.id = (:course_id) AND U.id = M.user_id ORDER BY M.id"
    result = db.session.execute(text(sql), {"course_id":course_id})
    return result.fetchall()

def get_user_from_course(id):
    sql = "SELECT U.id FROM courses C, users U " \
          "WHERE C.id = (:course_id) AND U.id = C.user_id"
    result = db.session.execute(text(sql), {"course_id":id})
    return result.fetchone()

def read_course_material(idd):
    sql = "SELECT C.textcontent FROM coursecontent C WHERE C.course_id = (:id)"
    sql2 = "SELECT C.title FROM courses C WHERE c.id = (:id)"
    result = db.session.execute(text(sql), {"id":idd})
    result2 = db.session.execute(text(sql2), {"id":idd})
    rivi = result.fetchone()
    rivi2 = result2.fetchone()
    if rivi and rivi2:
        return [rivi[0],rivi2[0]]
    else: return None


def delete_course(id):
    try:
        sql = "DELETE FROM courses C WHERE C.id = (:id);"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True
    except:
        db.session.rollback()
        print("AAAAA")
        return False
    
    
def search_content(id,id2):
    sql = "SELECT C.textcontent FROM coursecontent C WHERE C.course_id = (:id) AND C.pagenumber =  (:id2)"

    result = db.session.execute(text(sql), {"id":id, "id2":id2})

    #print(id)
    #print(id2)

    a = result.fetchall()

    if a:
        return a
    else:
        return None
    

def search_polls(id,id2):
    sql = "SELECT id, topic FROM polls C WHERE C.course_id = (:id) AND C.pagenumber =  (:id2)"
    

    result = db.session.execute(text(sql), {"id":id, "id2":id2})

    results = result.fetchall()

    if not results:
        return None
    
    all_polls = []

    for the_poll_id, topic in results:

        sql = "SELECT id, choice FROM choices WHERE poll_id=:id"
        result = db.session.execute(text(sql), {"id":the_poll_id})

        choices = result.fetchall()

        print(topic,choices)

        all_polls.append((topic, choices))

    print(all_polls)

    if not all_polls:
        return None
    else:
        return all_polls
    




def search_answers(course_id):

    sql = """SELECT a.id, c.choice, u.username, a.sent_at, p.topic
    FROM answers a
    LEFT JOIN choices c ON a.choice_id = c.id
    LEFT JOIN users u ON a.answered_by = u.id
    JOIN polls p ON c.poll_id = p.id
    WHERE p.course_id = (:course_id)
    ORDER BY a.sent_at"""

    courses_id_get = db.session.execute(text(sql), {"course_id":course_id}).fetchall()

    print(courses_id_get)

    return courses_id_get


def search_answers2(course_id, search):

    sql = """SELECT a.id, c.choice, u.username, a.sent_at, p.topic
    FROM answers a
    LEFT JOIN choices c ON a.choice_id = c.id
    LEFT JOIN users u ON a.answered_by = u.id
    JOIN polls p ON c.poll_id = p.id
    WHERE p.course_id = (:course_id) AND
    u.username LIKE :query
    ORDER BY a.sent_at"""

    courses_id_get = db.session.execute(text(sql), {"course_id":course_id, "query":"%"+search+"%"}).fetchall()


    return courses_id_get


def search_answered_users(course_id):

    sql = """SELECT COUNT(DISTINCT u.username), COUNT(u.username)
    FROM answers a
    LEFT JOIN choices c ON a.choice_id = c.id
    LEFT JOIN users u ON a.answered_by = u.id
    JOIN polls p ON c.poll_id = p.id
    WHERE p.course_id = (:course_id)"""

    courses_id_get = db.session.execute(text(sql), {"course_id":course_id}).fetchall()


    return courses_id_get






def send(content, description,textcontent):
    user_id = users.user_id()
    if user_id == 0:
        return False
    try:
        sql = "INSERT INTO courses (title, user_id, description, sent_at) VALUES (:content, :user_id, :description, NOW()) RETURNING id"

        sql2 = "INSERT INTO coursecontent (course_id, textcontent, pagenumber) VALUES (:course_id, :textcontent, 1)"

        courses_id_get = db.session.execute(text(sql), {"content":content, "user_id":user_id, "description":description}).fetchone()

        if courses_id_get:
            course_id = courses_id_get[0]
        else: return False

        db.session.execute(text(sql2), {"course_id":course_id, "textcontent":textcontent})

        db.session.commit()
        return True
    except:
        return False
