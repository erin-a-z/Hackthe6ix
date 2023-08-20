from taipy.gui import Gui, notify
root_md = """
<|layout|columns=auto|
<|part|class_name=m-auto|

# Recyclonnect  # {: .text-center}

<|content|>

This application was created with [Taipy](https://www.taipy.io/).
|>
|>
"""
page1_md="""
## We are a organization that certifies the product that are actually recyclable.
[link](page2qw)
 """
page2_md="## This is page 2"

pages = {
    "/": root_md,
    "page1": page1_md,
    "page2": page2_md
}
Gui(pages=pages).run(use_reloader=True, port=1200)

# Gui(page, css_file='frontend/style.css').run(use_reloader=True, port=1200)