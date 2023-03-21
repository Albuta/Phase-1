n = input("please enter text : \n")
if n == "":
    print ("please enter text : \n")
    b = input("")
    print("number of characters in " + b, "is", (len(b)))
else:
    print("number of characters in " + n, "is", (len(n)))
