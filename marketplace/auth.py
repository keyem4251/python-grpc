import os
import pyrebase

API_KEY = os.getenv("API_KEY")
AUTH_DOMAIN = os.getenv("AUTH_DOMAIN")
PROJECT_ID = os.getenv("PROJECT_ID")
STORAGE_BUCKET = os.getenv("STORAGE_BUCKET")
MESSAGING_SENDER_ID = os.getenv("MESSAGING_SENDER_ID")
APP_ID = os.getenv("APP_ID")
MEASUREMENT_ID = os.getenv("MEASUREMENT_ID")


def init_auth():
    firebase_config = {
        "apiKey": API_KEY,
        "authDomain": AUTH_DOMAIN,
        "projectId": PROJECT_ID,
        "storageBucket": STORAGE_BUCKET,
        "messagingSenderId": MESSAGING_SENDER_ID,
        "appId": APP_ID,
        "measurementId": MEASUREMENT_ID,
    }
    firebase = pyrebase.initialize_app(firebase_config)
    return firebase.auth()
