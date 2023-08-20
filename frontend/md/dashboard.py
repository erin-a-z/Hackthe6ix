page5_md = """
# Dashboard
Enter new code:
<|{code}|input|class=text-center|> 

<|Submit Code|button|on_action=checkCode|>

Points: <|{code}|>
<|{points}|chart|>
<|{data}|chart|x=x_col|y[1]=y_col_1|y[2]=y_col_2|color[1]=green|>
"""