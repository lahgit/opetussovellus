CREATE TABLE visitors (id SERIAL PRIMARY KEY, time TIMESTAMP);
CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE courses ( id SERIAL PRIMARY KEY, title TEXT UNIQUE, description TEXT, user_id INTEGER REFERENCES users, sent_at TIMESTAMP);
CREATE TABLE coursecontent (id SERIAL PRIMARY KEY, course_id INTEGER REFERENCES courses, textcontent TEXT);