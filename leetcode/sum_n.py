# Using Iteration

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9]))

def listsum(numList):
    sum = 0
    for i in range(len(numList)):
        sum += numList[i]
    return sum

print(listsum([1,3,5,7,9]))

# Using Recursion

def sumrec(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sumrec(numList[1:])

print(sumrec([1, 3, 5, 7, 9]))

