def digits(num :str):
    digits_list = []
    for n in num:
        digits_list.append(int(n))
    
    return digits_list

def addDigits(numList):
    return sum(numList)

numList = digits("52")

print(addDigits(numList))