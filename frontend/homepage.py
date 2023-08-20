from taipy.gui import Gui, notify, navigate
import magic
from md.landing import page1_md
from md.login import page2_md
from md.about import page3_md
from md.constant import root_md

def loginPage(state):
    navigate(state, "login")

def loginButtonAction(state):
    notify(state, 'Login:', "Running Login Function")

pages = {
    "/": root_md,
    "landing": page1_md,
    "login": page2_md,
    "about": page3_md,
}
Gui(pages=pages).run(use_reloader=True, port=1200)

# Gui(page, css_file='frontend/style.css').run(use_reloader=True, port=1200)



