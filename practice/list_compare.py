import sys

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 7, 10]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def compareLists(firstList, latterList):
    result = []
    if(len(firstList) > len(latterList)):
        # first list is larger
        for val in firstList:
            if val in latterList:
                result.append(val)

    else:
        for val in latterList:
            if val in firstList:
                result.append(val)

    return result


print(*str(compareLists(a, b)))
