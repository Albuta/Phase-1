name = input("Please enter your name: ")
first_letter = name[0].upper()

if first_letter == "A":
    greeting = "Hi!"
elif first_letter == "B":
    greeting = "Hello!"
elif first_letter == "C":
    greeting = "Hey!"
else:
    greeting = "Nice to meet you "

print(greeting + name)