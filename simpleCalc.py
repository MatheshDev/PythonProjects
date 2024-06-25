print("This is a simple calculator built using Python")

num1 = int(input("Enter A Value : ")) 
num2 = int(input("Enter B value : "))

print("1 - Add \n 2 - Sub \n 3 - Mul \n 4 - Div \n 5 - Mod \n")
operation = int(input("Enter the operation number you want to perform : "))

if(operation == 1):
    print(f"The Sum of {num1} and {num2} is ",num1 + num2)
elif(operation == 2):
    print(f"The Difference of {num1} and {num2} is ",num1-num2)
elif(operation == 3):
    print(f"The Multiplication of {num1} and {num2} is ", num1*num2)
elif(operation == 4):
    print(f"The Division of {num1} and {num2} is ", num1/num2)
elif(operation == 5):
    print(f"The Modulas of {num1} and {num2} is ", num1%num2)
else:
    print("Please enter the number within the Range")