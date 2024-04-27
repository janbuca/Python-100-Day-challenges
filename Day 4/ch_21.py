# Who will pay the bill
import random
name_string = input("Given everybody's name's speared by a comma. ")
# Split the string into a list
names = name_string.split(", ")
# Get the length of the list
num_items = len(names)
# Generate a random number between 0 and the last index
random_choice = random.randint(0, num_items - 1)
# Pick out random person from list of names using the random number
person_who_will_pay = names[random_choice]  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print(f"{person_who_will_pay} is going to buy the meal today!")