num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter operation(*,/,+,-):")
if operation == "+":
    result=num1+num2
    print(f"SUM: {result}")
elif operation =="-":
    result=num1-num2
    print(f"difference:{result}")
elif operation =="*":
    result=num1*num2
    print(f"product:{result}")
elif operation =="/":
    if num2 == 0:
        print("Error")
    else:
        result=num1/num2
        print(f"quotient:{result}")
elif operation =="%":
    result= num1%num2
    print(f"remainder:{result}")
else:
    print("Invalid operation")        

       