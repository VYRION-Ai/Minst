import telepot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime, time
from firebase import firebase
import pyrebase
import argparse
from google.colab import drive
import matplotlib.pyplot as plt
import cv2

# telegram
# Replace with your token
token = '1944147483:AAFz_reVI6EtLhK8bRoHfHjjf29JqtRxQY0'  # telegram token
# Replace with your receiver id
receiver_id = 1266606453  # https://api.telegram.org/bot1944147483:AAFz_reVI6EtLhK8bRoHfHjjf29JqtRxQY0/getUpdates
bot = telepot.Bot(token)
bot.sendMessage(receiver_id, 'Your camera is active now.')  # send a message on telegram

# Firebase

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://becarful-canada-default-rtdb.firebaseio.com/'
})

ref = db.reference('')
users_ref = ref.child('Images')

config = {
    "apiKey": "ae04102012555bfcae7ebdae8b6c9ea38ae2eb3f",
    "authDomain": "https://accounts.google.com/o/oauth2/auth",
    "databaseURL": "https://becarful-canada-default-rtdb.firebaseio.com/",
    "projectId": "becarful-canada",
    "storageBucket": "becarful-canada.appspot.com",
    "messagingSenderId": "104645753169902597075"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def save1(date_,imgg,url, number):
    args = parser.parse_args()
    #my_image = args.source
    storage.child("Images").child(url).put(imgg)
    #time.sleep(1)
    users_ref.push().set({
        'number': number,
        'url': url,
        'date': date_,
    })


parser = argparse.ArgumentParser()
parser.add_argument('--source', type=str, default='inference/images', help='source')  # file/folder, 0 for webcam
parser.add_argument('--names', type=str, default='data/coco.names', help='*.cfg path')
opt = parser.parse_args()
print(opt)