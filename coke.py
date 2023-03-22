accepted_coins = [25, 10, 5]
price = 50
inserted_amount = 0

while inserted_amount < price:
    coin = int(input("Insert a coin (25, 10, or 5 cents): "))
    if coin in accepted_coins:
        inserted_amount += coin
        print("Amount due:", abs(price - inserted_amount), "cents")
    else:
        print("Invalid coin. Please insert 25, 10, or 5 cents.")

change = abs(inserted_amount - price)
if change > 0:
    print("change owned ", change, "cents")
else:
    print("Thank you for your purchase!")
