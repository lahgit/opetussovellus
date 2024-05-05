# opetussovellus
Tietokannat ja web-ohjelmointi kurssi.


Sovelluksen idea on antaa käyttäjien luoda kursseja, suorittaa kursseja ja saada/antaa arvosana suorituksesta.

- [x] Pystyy Rekisteröitymään, kirjautumaan ja kirjautumaan ulos
- [x] Pystyy Lisäämään kursseja
- [x] Kursseille pystyy lisäämään eri sivuille tekstimateriaalia ja kyselyjä
- [x] Materiaaleja voi olla useampi yhtä sivuakohden
- [ ] Materiaaleja voi laittaa järjestykseen



Guide:

Create a new folder:

`$ mkdir app`
`$ cd app`

Clone repository
`$ git init`
`$ git clone https://github.com/lahgit/opetussovellus.git`

Create environment

`$ python3 -m venv venv`

`$ source venv/bin/activate`

Install requirements
`$ pip install -r requirements.txt`

Import schema:

`$ psql < schema.sql`

`create .env file`

and instert

DATABASE_URL=postgresql:///{user}
SECRET_KEY={secret_key}

Run application

`$ flask run`

