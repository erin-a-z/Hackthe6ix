from taipy.gui import Gui, notify
import pandas as pd

email = ""
password = ""



# Definition of the page
page = """
# Login # {: .text-center}
Email: <|{email}|input|classname=text-center|> 
{: .text-center}

Password: <|{password}|input|>
{: .text-center}

<|Run local|button|on_action=loginButtonAction|>
{: .text-center}


"""

def loginButtonAction(state):
    notify(state, 'Login:', "Running Login Function")


Gui(page, css_file='frontend/style.css').run(use_reloader=True, port=1200)