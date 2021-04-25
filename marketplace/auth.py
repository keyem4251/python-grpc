import os
import json
import pyrebase

FIREBASE_CONFIG_FILE = os.getenv("FIREBASE_CONFIG_FILE", None)


def init_auth():
    with open(FIREBASE_CONFIG_FILE) as f:
        firebase_config = json.loads(f.read())
    firebase = pyrebase.initialize_app(firebase_config)
    return firebase.auth()
