from pyfcm import FCMNotification
from firebase_controller import get_all_players

def send_notification(token, name):
    push_service = FCMNotification(
        api_key="AAAAVb5JwQI:APA91bHd-4Rwk92cEDP7vew-iCmKwx5V92KKLsNOaPkya8pF4AhzmmIi29JC3xrqBj3mNHHUO4Y7zVaYqyurtEP1m-PH_eUUcZcMsH2o7ZugxNvTnKImmVReNKXJ4dh-YNL5d_DcXjCG")
    registration_id = token
    message_title = "Hello " + name
    message_body = "This is a notification from Flask Backend"
    data_message = {
        "notification": "true"
    }

    push_service.notify_single_device(registration_id=registration_id,
                                               message_title=message_title,
                                               message_body=message_body,
                                               data_message=data_message)


def send_notification_to_all():
    players = get_all_players()
    for player in players:
        send_notification(token=player['fcm_token'], name=player['facebook_name'])
    return
