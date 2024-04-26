#  # BMI Calculator 
# height = float(input("Enter your height in m: "));
# weight = float(input("Enter your weight in kg: "));
# bmi = round(weight / height ** 2);

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight.");

# elif bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight.");

# elif bmi < 30:
#     print(f"Your BMI is {bmi}, you are slightly overweight.");

# elif bmi < 35:
#     print(f"Your BMI is {bmi}, you are obese.");

# else:
#     print(f"Your BMI is {bmi}, you are clinically obese.")


# This is a Difficult Challenge
# Leap Year Calculator 
# year = int(input("Which year do you want to check? "));


# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.");
#         else:
#             print("Not leap year.");
#     else:
#         print("Leap year.");
# else:
#     print("Not leap year.");


# This is a Difficult Challenge
# Password Generator Project
# import random

year = int(input("What year do you want to check "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
     