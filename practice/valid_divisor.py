import sys
import math


def allValidDivisors(input):
    result = []
    possible_valid_divisors = range(2, math.ceil(math.sqrt(input))+1)
    for possible_divisor in possible_valid_divisors:
        if(input % possible_divisor == 0):
            result.append(possible_divisor)

    return result


user_input = int(input("Enter a number to check for valid divisors: "))

print(*str(allValidDivisors(user_input)))
