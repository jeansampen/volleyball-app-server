from firebase_controller import get_db_ref

def store_match_into_db(match):
    db = get_db_ref()
    db.child('matches').push(match)
    return


def get_all_matches_from_db():
    db = get_db_ref()
    return db.child('matches').get().val()


def delete_match_from_db(id):
    raise NotImplementedError
