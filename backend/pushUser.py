import pyrebase

config = {
  "apiKey": "AIzaSyBcNTA0SpIrrMaihnfNMv31U0ScZv6xqFo",
  "authDomain": "recyclonnect.firebaseapp.com   ",
  "databaseURL": "https://recyclonnect-default-rtdb.firebaseio.com",
  "storageBucket": "recyclonnect.appspot.com"
}

firebase = pyrebase.initialize_app(config)

###Definitions

def addUser(username, password):
  #Connecting to firebase real time db
  db = firebase.database()

  #Pushing guest user
  db.child("users").child(username)
  data = {"password": password}
  db.set(data);




##### Running
addUser("Test User2", "badpassword")