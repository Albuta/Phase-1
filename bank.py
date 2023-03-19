print("greet me")
grtng = input("")
#greeting starts with hello, display $0
if grtng == "hello":
    print("you have $0")
#greeting starts with h but it's not hello, display $20
elif grtng[0] == "h" and grtng != "hello":
    print("you have $20")
#greeting doesn't start with h, display $100
else:
    print("you have $100")
