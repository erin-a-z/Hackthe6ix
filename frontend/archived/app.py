from taipy.gui import Gui, notify
from login import login_page
login_page = login_page()
page = """
<|layout|columns=auto|
<|part|class_name=m-auto|

# Recyclonnect  # {: .text-center}
We are a organization that certifies the product that are actually recyclable.
<br/>
<p><a href="login_page" class="foo bar" title="Some title!">link</a></p>
|>
|>
"""

def login(state):
    notify(state, 'Login:', "Running Login Function")

Gui(page, css_file='frontend/style.css').run(use_reloader=True, port=1200)