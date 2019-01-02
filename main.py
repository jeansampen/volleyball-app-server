from flask import Flask, request, jsonify
from flask_cors import CORS
from player_controller import store_player_in_db, get_all_players_from_db, delete_player_from_db
from match_controller import store_match_into_db, get_all_matches_from_db, delete_match_from_db
from pyfcm import FCMNotification
import pyrebase

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "welcome to the volleyball app api"


@app.route('/about')
def about():
    return "here will be the documentation of the app"


# User API
@app.route('/get-players', methods=['GET'])
def get_players():
    return jsonify(get_all_players_from_db())


@app.route('/store-player', methods=['POST'])
def store_player():
    store_player_in_db(request.get_json())
    return "Storing player {} into the database".format(request.get_json())


@app.route('/delete-player/<int:id>', methods=['DELETE'])
def delete_player(id):
    delete_player_from_db(id)
    return "Deleting item with id = {} ".format(id)


# Match API
@app.route('/get-matches', methods=['GET'])
def get_matches():
    return jsonify(get_all_matches_from_db())


@app.route('/store-match', methods=['POST'])
def store_match():
    store_match_into_db(request.get_json())
    return "Storing the given match"


@app.route('/delete-match/<int:id>', methods=['DELETE'])
def delete_match(id):
    delete_match_from_db(id)
    return "Deleting match with id {}".format(id)

@app.route('/test-firebase/<string:text>')
def test_firebase(text):
    config = {"apiKey": "AIzaSyDATfDOl4x1fvxMh-pwQPAbd0XzZMOS30w",
              "authDomain": "volley-ball-app.firebaseapp.com",
              "databaseURL": "https://volley-ball-app.firebaseio.com/",
              "storageBucket": "volley-ball-app.appspot.com",
              }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child("node1").push({"text": text})
    return "successfully tested firebase, I guess..."



if __name__ == '__main__':
    app.run(debug=True)
