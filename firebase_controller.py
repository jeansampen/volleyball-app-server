import pyrebase


def get_db_ref():
    config = {"apiKey": "AIzaSyDATfDOl4x1fvxMh-pwQPAbd0XzZMOS30w",
              "authDomain": "volley-ball-app.firebaseapp.com",
              "databaseURL": "https://volley-ball-app.firebaseio.com/",
              "storageBucket": "volley-ball-app.appspot.com",
              }
    firebase = pyrebase.initialize_app(config)
    return firebase.database()


def get_all_players():
    db = get_db_ref()
    return list(db.child('players').get().val().values())
