def checkNum(num):
    if(num % 2 == 0):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

a = int(input("Enter a number : "))
checkNum(a)