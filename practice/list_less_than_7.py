import sys

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
result = []

for val in a:
    if(val < 7):
        if val not in result:
            result.append(val)


print(*str(result))
