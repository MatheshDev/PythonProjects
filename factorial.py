def Factorial(num):
    if(num <= 1):
        return 1
    else:
        print(num ,"x" ,num-1)
        result  = num * Factorial(num-1)
        return result


print(Factorial(4))