import pyrebase

config = {
  "apiKey": "AIzaSyBcNTA0SpIrrMaihnfNMv31U0ScZv6xqFo",
  "authDomain": "recyclonnect.firebaseapp.com   ",
  "databaseURL": "https://recyclonnect-default-rtdb.firebaseio.com",
  "storageBucket": "recyclonnect.appspot.com"
}

firebase = pyrebase.initialize_app(config)


auth=firebase.auth()


def signup(email, password):
    try:
        user=auth.create_user_with_email_and_password(email, password)
        print(user)
        print("Successfully Created account")
        return user
    except:
        print("Email already exists")
    

def login(email, password):
    try:
        login=auth.sign_in_with_email_and_password(email, password)
        print(login)
        print("Successfully Logged in account")
        return login
    except:
        print("Email or password invalid!!!")

login("test@gmail.com", " password")