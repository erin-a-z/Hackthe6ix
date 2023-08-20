import pyrebase

config = {
  "apiKey": "AIzaSyBcNTA0SpIrrMaihnfNMv31U0ScZv6xqFo",
  "authDomain": "recyclonnect.firebaseapp.com   ",
  "databaseURL": "https://recyclonnect-default-rtdb.firebaseio.com",
  "storageBucket": "recyclonnect.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#Connecting to firebase real time db
db = firebase.database()


#Pushing guest user
db.child("users").child("Guest2")

data = {"name": "Guest2 Name"}

db.child("users").push(data);