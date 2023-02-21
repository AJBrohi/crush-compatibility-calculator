print("Welcome to the Crush Compatibility Calculator!\n")
name1 = input("What is your name? \n->").lower()
name2 = input("What is their name? \n->").lower()

combined_name = name1 + " "+ name2

first_digit = combined_name.count('t') + combined_name.count('r') + combined_name.count('u') + combined_name.count('e')

second_digit = combined_name.count('l') + combined_name.count('o') + combined_name.count('v') + combined_name.count('e')

score = int(f"{first_digit}{second_digit}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
    
elif score > 40 and score < 50:
    print(f"Your score is {score}, there's a little risk.")
    
else:
    print(f"Your score is {score}, you guys will be alright together.")
