while True:
    fuel = input("Fraction: ")
    try:
        num1, num2 = fuel.split("/")
        new_num1 = int(num1)
        new_num2 = int(num2)
        f = new_num1 / new_num2
        if f<=1:
            break
    except (ValueError, ZeroDivisionError):
        pass
p = int(f*100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
