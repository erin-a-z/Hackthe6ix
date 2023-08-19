from taipy.gui import Gui, notify
import pandas as pd

email = ""
password = ""



# Definition of the page
page = """



<|layout|columns=auto|
<|part|class_name=m-auto|

# Login # {: .text-center}
Email: <|{email}|input|class=text-center|> 


Password: <|{password}|input|>

<|Run local|button|on_action=loginButtonAction|>
|>
|>
"""

def loginButtonAction(state):
    notify(state, 'Login:', "Running Login Function")


Gui(page, css_file='frontend/style.css').run(use_reloader=True, port=1200)