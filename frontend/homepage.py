from taipy.gui import Gui, notify, navigate
import magic
from md.landing import page1_md
from md.login import page2_md
from md.about import page3_md
from md.signup import page4_md
from md.dashboard import page5_md
from md.constant import root_md

import sys
import os

# Get the path of the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the sys.path
sys.path.append(parent_dir)

# Now you can import something.py from the backend folder
from backend.pyrebaseAuth import login,signup

codes = ["1111", "2222"]

userPoints = 5
code = 0
points = 0
email = ""
password = ""
# login
def lol(state):
    # print(f'{state.email} {state.password}')
    result = login(state.email, state.password)
    print(result["idToken"])
    if result["idToken"] != "":
        print("success")
        notify(state, 'Login:', "Successfully Logged in account")
        navigate(state,"dash")

# sign up
def sigh(state):
    result = signup(state.email, state.password)
    print(result["idToken"])
    if result["idToken"] != "":
        print("success")
        notify(state, 'Login:', "Successfully Created account")
        navigate(state,"login")

# catch error
def on_exception(state, fct_name, e):
    notify(state, "error", f"Error accessing your account")

# landing page redirecting to sign up
def signUpPage(state):
    navigate(state, "signup")

# landing page redirecting to login
def loginPage(state):
    navigate(state, "login")

def checkCode(state):
    newCode = state.code

    for code in codes:
        
        if code == newCode:
            notify(state, "error", f"Code already exists")
            return
    codes.append(newCode)
    print(codes)
    notify(state, 'Code Valid:', "Successfully added points")
    #add to a point counter
    state.points +=1
    print("Userpoints: ", userPoints)
    print("Points: ", state.points)
    return

# dashboard graphs
list_to_display = [100/x for x in range(1, 100)]
data = {"x_col":[0,1,2], "y_col_1":[4,2,1], "y_col_2":[3,1,2]}
pages = {
    "/": root_md,
    "landing": page1_md,
    "login": page2_md,
    "about": page3_md,
    "signup": page4_md,
    "dash": page5_md,
}
Gui(pages=pages).run(use_reloader=True, port=1200)

# Gui(page, css_file='frontend/style.css').run(use_reloader=True, port=1200)



