user_input = input("enter text: ")
text = "aeiouAEIOU"
result = ""

for char in user_input:
    if char not in text:
        result += char


print(result)
