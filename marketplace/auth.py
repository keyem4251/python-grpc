import os
import pyrebase

  API_KEY = os.getenv("API_KEY")
  AUTH_DOMAIN = os.getenv("API_KEY")
  PROJECT_ID = os.getenv("API_KEY")
  STORAGE_BUCKET = os.getenv("API_KEY")
  MESSAGING_SENDER_ID = os.getenv("API_KEY")
  APP_ID = os.getenv("API_KEY")
  MEASUREMENT_ID = os.getenv("API_KEY")


def init_auth():
    firebase_config = {
        "apiKey": API_KEY,
        "authDoamin": AUTH_DOMAIN,
        "projectId": PROJECT_ID,
        "storageBucket": STORAGE_BUCKET,
        "messagingSenderId": MESSAGING_SENDER_ID,
        "appId": APP_ID,
        "measurementId": MEASUREMENT_ID,
    }
    firebase = pyrebase.initialize_app(firebase_config)
    return firebase.auth()
