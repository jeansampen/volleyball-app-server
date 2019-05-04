from flask import Flask, request, jsonify
from flask_cors import CORS
from player_controller import store_player_in_db, get_all_players_from_db, delete_player_from_db
from event_controller import store_event_into_db, get_all_events_from_db, delete_event_from_db
from notification_service import send_notification_to_all

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return "welcome to the volleyball app api"


@app.route('/about')
def about():
    return "here will be the documentation of the app"


# User API
@app.route('/player', methods=['GET'])
def get_players():
    return jsonify(get_all_players_from_db())


@app.route('/player', methods=['POST'])
def store_player():
    store_player_in_db(request.get_json())
    return "Storing player {} into the database".format(request.get_json())


@app.route('/delete-player/<int:id>', methods=['DELETE'])
def delete_player(id):
    delete_player_from_db(id)
    return "Deleting item with id = {} ".format(id)


# Match API
@app.route('/event', methods=['GET'])
def get_matches():
    return jsonify(get_all_events_from_db())


@app.route('/event', methods=['POST'])
def store_match():
    store_event_into_db(request.get_json())
    return "Storing the given event"


@app.route('/delete-match/<int:id>', methods=['DELETE'])
def delete_match(id):
    delete_event_from_db(id)
    return "Deleting event with id {}".format(id)

@app.route('/notify')
def notify():
    send_notification_to_all()
    return "notifying all players"


if __name__ == '__main__':
    app.run(debug=True)
