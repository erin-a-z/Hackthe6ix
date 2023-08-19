from taipy.gui import Gui, notify
import pandas as pd

email = ""
password = ""




# Definition of the page
page = """The text is:
# Login

Email: <|{email}|input|>

Password: <|{password}|input|>

<|Run local|button|on_action=loginButtonAction|>

"""

def loginButtonAction(state):
    notify(state, 'Login:', "Running Login Function")


Gui(page).run(use_reloader=True)