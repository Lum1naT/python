import sys


def is_even(input):
    if(input % 2 == 0):
        return True
    else:
        return False


user_input = int(input("Zadejte celé číslo: "))
print(is_even(user_input))
