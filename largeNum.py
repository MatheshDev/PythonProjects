numList = [2,6,8,5,3]

def LargeNum(numList):
    large = numList[0]
    for num in numList:
        if num > large:
            large = num
    return large

print(LargeNum(numList))