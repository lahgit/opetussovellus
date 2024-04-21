DROP TABLE users CASCADE;
DROP TABLE courses CASCADE;
DROP TABLE coursecontent;

DROP TABLE answers;
DROP TABLE choices;
DROP TABLE polls;



CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT);
CREATE TABLE courses ( id SERIAL PRIMARY KEY, title TEXT UNIQUE, description TEXT, user_id INTEGER REFERENCES users ON DELETE CASCADE, sent_at TIMESTAMP);
CREATE TABLE coursecontent (id SERIAL PRIMARY KEY, course_id INTEGER REFERENCES courses ON DELETE CASCADE, textcontent TEXT, pagenumber INTEGER);

CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES courses ON DELETE CASCADE,
    pagenumber INTEGER,
    topic TEXT,
    created_at TIMESTAMP
);

CREATE TABLE choices (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls ON DELETE CASCADE,
    choice TEXT
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    choice_id INTEGER REFERENCES choices ON DELETE CASCADE,
    answered_by INTEGER REFERENCES users ON DELETE CASCADE,
    sent_at TIMESTAMP
);
