quotes = {
    "Nelson Mandela": "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "Walt Disney": "The way to get started is to quit talking and begin doing",
    "Benjamin Franklin": "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
    "Mae West": "You only live once, but if you do it right, once is enough.",
    "Obi-Wan Kenobi": "These aren't the droids you're looking for."
}

quote = input("What is the quote? ")
author = input("Who said it? ")

if author in quotes and quote == quotes[author]:
    print(f"{author} says, \"{quote}\"")
else:
    print("Wrong quote")
