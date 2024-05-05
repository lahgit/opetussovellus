# opetussovellus
Tietokannat ja web-ohjelmointi kurssi.


Sovelluksen idea on antaa käyttäjien luoda kursseja, suorittaa kursseja ja saada/antaa arvosana suorituksesta.

- [x] Pystyy Rekisteröitymään, kirjautumaan ja kirjautumaan ulos
- [x] Salasana pitää olla ainakin 8 merkkiä ja käyttäjänimi ei saa olla tyhjä
- [x] Pystyy Lisäämään kursseja
- [x] Kursseille pystyy lisäämään eri sivuille tekstimateriaalia ja kyselyjä
- [x] Materiaaleja voi olla useampi yhtä sivua kohden
- [ ] Materiaaleja voi laittaa järjestykseen
- [x] Kursseja voi poistaa
- [ ] Yksittäisiä materiaaleja voi poistaa
- [ ] Kursseja voi etsiä hakutoiminnolla
- [x] Oman kurssin vastaajia voi nimeltä etsiä hakutoiminnolla
- [x] Kyselyiden vastauksia voi lukea kurssin tekijä
- [x] Kurssin tekijä voi lähettää haluamansa arvosanan käyttäjile
- [x] Käyttäjä voi tarkastella saamiaan arvosanoja
- [ ] Arvosanan lisäämistä varten on estoja jotka estävät laittamasta liikaa arvosanoja ja laittamasta niitä kenelle sattuu
- [x] Vastaussivulla Näkyy monta eri käyttäjää ja monta vastausta siellä on


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

