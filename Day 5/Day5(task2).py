age = int(input("Enter your age: "))
income = int(input("Enter your income: "))
credit_score = int(input("Enter your credit score"))
if age<18 and income<30000 and credit_score<600:
    print("You are not eligible for a loan")
else:    
     print("You are eligible for a loan")    