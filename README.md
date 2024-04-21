# opetussovellus
Tietokannat ja web-ohjelmointi kurssi.


Sovelluksessa voi lisätä käyttäjiä ja kursseja. Tällä hetkellä materiaalin lisääminen toimii osittain ja kurssien poistaminen toimii.

Ulkoasu ei ole täysin valmis.



guide:

create a new folder:

$ mkdir app
$ cd app

clone repository
$ git init
$ git clone https://github.com/lahgit/opetussovellus.git

create environment

$ python3 -m venv venv

$ source venv/bin/activate

install requirements
$ pip install -r requirements.txt

import schema:

$ psql < schema.sql

create .env file

and instert

DATABASE_URL=postgresql:///{user}
SECRET_KEY={secret_key}

run application

$ flask run
