import pyrebase


def get_db_ref():
    config = {"apiKey": "AIzaSyDATfDOl4x1fvxMh-pwQPAbd0XzZMOS30w",
              "authDomain": "volley-ball-app.firebaseapp.com",
              "databaseURL": "https://volley-ball-app.firebaseio.com/",
              "storageBucket": "volley-ball-app.appspot.com",
              }
    firebase = pyrebase.initialize_app(config)
    return firebase.database()
