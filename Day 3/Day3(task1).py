user_name=input("Enter your name:")
user_age=int(input("Enter your age:"))
if user_age < 0:
    print(f"You cannot age backwords!{user_name}")
elif user_age<13:
    print(f"You are a child!{user_name}")
elif user_age<18:
    print(f"You are a teenager!{user_name}")
elif user_age<65:
    print(f"You are an adult!{user_name}")
else:
    print(f"You are a senior citizen!{user_name}")