import time
import math
import json
import firebase_admin
from firebase_admin import db

cred = firebase_admin.credentials.Certificate("heartbeat-78631-firebase-adminsdk-z2keb-b9bbff6afe.json")
default_app = firebase_admin.initialize_app(cred, {
    "databaseURL": "https://heartbeat-78631-default-rtdb.asia-southeast1.firebasedatabase.app/"
	})

ref = db.reference("/")

count = 0.0
while(count <= 5.0):
    x = math.sin(count)
    ref.push().set(x)
    print(count, x)
    count += 0.1
    time.sleep(0.1)