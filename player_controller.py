import sqlite3


def store_player_in_db(user):
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    nickname = user.get('nickname')
    token = user.get('token')
    c.execute('INSERT INTO players(nickname, token) VALUES(?,?)', [nickname, token])
    conn.commit()
    return


def get_all_players_from_db():
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    results = c.execute('SELECT * FROM players').fetchall()
    return results


def delete_player_from_db(id):
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    c.execute("DELETE FROM players WHERE (id = ?)", [id])
    conn.commit()
    return "Successfully deleted player with id {} from DB".format(id)


def init_players():
    conn = sqlite3.connect('volleyball.db')
    c = conn.cursor()
    c.execute('CREATE TABLE players ('
              'id INTEGER PRIMARY KEY AUTOINCREMENT,'
              'nickname VARCHAR(50),'
              'token DATETIME'
              ')')

