import pyrebase

config = {
  "apiKey": "AIzaSyBcNTA0SpIrrMaihnfNMv31U0ScZv6xqFo",
  "authDomain": "recyclonnect.firebaseapp.com   ",
  "databaseURL": "https://recyclonnect-default-rtdb.firebaseio.com",
  "storageBucket": "recyclonnect.appspot.com"
}

firebase = pyrebase.initialize_app(config)

firebase.database()