from firebase_controller import get_db_ref

def store_event_into_db(event):
    db = get_db_ref()
    db.child('events').push(event)
    return


def get_all_events_from_db():
    db = get_db_ref()
    return db.child('events').get().val()


def delete_event_from_db(id):
    raise NotImplementedError
