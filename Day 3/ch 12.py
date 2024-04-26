# # Odd or Even Exercise
# print("Enter any natural number? ");
# num = int(input("The Entering Number is "));
# if (num % 2 == 0):
#     print("This is even Number");
# else:
#     print("This is an Odd Number");

# # Nested if else
# print("Enter any natural number? ");
# num = int(input("The Entering Number is "));
# if (num % 2 == 0):
#     print("This is even Number");
#     if (num % 4 == 0):
#         print("This is a multiple of 4");
#     else:
#         print("This is not a multiple of 4");
# else:
#     print("This is an Odd Number");


# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are an adult")
#     if age >= 65:
#         print("You are a senior citizen")
#     else:
#         print("You are not a senior citizen")
# else:
#     print("You are not an adult")

age = int(input("What is your age? "))
if age < 12:
    print("Please pay $5.")
elif age <= 18:
    print ("Please pay $7.")
else:
    print("Please pay $12.")