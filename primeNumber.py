def checkPrime(num):
    if(num <= 1):
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

primeSet = []

def addPrime(n : int):
    for num in range(0,n+1):
        if(checkPrime(num)):
            primeSet.append(num)
    return primeSet

print(addPrime(11))
