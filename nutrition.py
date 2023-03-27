#list of fruits
fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 50,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangarine" : 50,
    "watermelon" : 80

}
#user input
user_choice = input("Item: ")
#loop for each fruit so we could identify specific fruit
for f in fruits:
    if f in user_choice.lower():
#print fruit calories depending on user's choice
        print("Callories:", fruits[f])
