import webbrowser
with open("data", "r") as f:
    a=f.read()
webbrowser.open(a, new=1)
