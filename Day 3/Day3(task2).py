grades=float(input("enter the grades: "))
if grades<0 or grades>100:
    print("invalid grades")
elif grades>=90:
    message="excellent"
    grade="A"
elif grades>=80:
    message="Good Job"
    grade="B"
elif grades>=70:
    message="Think more"
    grade="C"
elif grades>=60:
    message="You need to work hard"
    grade="D"
else:    
    message="You failed"
    grade="F"

    print(f"Your grade is {grade} and {message}")
       

