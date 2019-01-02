from firebase_controller import get_db_ref


def store_player_in_db(user):
    db = get_db_ref()
    db.child('players').push(user)
    return


def get_all_players_from_db():
    db = get_db_ref()
    return db.child('players').get().val()


def delete_player_from_db(id):
    raise NotImplementedError

