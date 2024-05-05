# opetussovellus
Tietokannat ja web-ohjelmointi kurssi.


Sovelluksessa voi lisätä käyttäjiä ja kursseja. Kursseihin voi lisätä tekstimateriaaleja ja kyselyitä tai myös poistaa kokonaan.
Kurssin tekijä voi katsoa käyttäjien antamia vastauksia ja antaa arvosanoja kursseille. Kurssin tekijä voi käyttää vastaussivulla olevaa hakutoimintoa etsiäkseen käyttäjiä nimeltä.




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

