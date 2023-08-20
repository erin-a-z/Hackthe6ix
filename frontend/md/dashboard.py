page5_md = """
# Dashboard
Enter new code:
<|{code}|input|class=text-center|> 

<|Submit Code|button|on_action=checkCode|>

Points: <|{code}|>
<|{points}|chart|> <|{data}|chart|x=year|y[1]=Canada|y[2]=USA|color[1]=green|>
"""