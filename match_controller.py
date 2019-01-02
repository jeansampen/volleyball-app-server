import sqlite3
from datetime import datetime


def store_match_into_db(match):
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    place = match.get('place')
    date = datetime.strptime(match.get('date'), '%d.%m.%Y-%H:%M')
    c.execute('INSERT INTO matches(place, date) VALUES (?, ?)', [place, date])
    conn.commit()
    return


def get_all_matches_from_db():
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    return c.execute('SELECT * FROM matches').fetchall()


def delete_match_from_db(id):
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    c.execute('DELETE FROM matches WHERE(id = ?)', [id])
    conn.commit()
    return


def init_matches():
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    c.execute('CREATE TABLE matches ('
              'id INTEGER PRIMARY KEY AUTOINCREMENT,'
              'place VARCHAR(50),'
              'date DATETIME'
              ')')


