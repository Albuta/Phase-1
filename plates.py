def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if len(s) < 2:
        return False
    if len(s) > 6:
        return False
    if  s[:2].isalpha():
        return True
    if s[0].isdigit():
        return False
    if s[-1].isdigit():
        return False
    else:
        return False

main()
