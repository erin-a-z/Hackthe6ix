from taipy.gui import Gui, notify

email = ""
password = ""

login_page = """
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

Gui(login_page, css_file='frontend/style.css').run(use_reloader=True, port=1200)

def login_page():
    return login_page