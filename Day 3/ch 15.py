# Pizza Order Exercise
print("Welcome to Python Pizza Deliveries!") 
print ("\tSmall size Pizza: $15 \t\t\n Medium size pizza: $20 \t\t\n Large pizza: $25");
size = input("What Size pizza do you want? S, M, or L:  ")
print ("\t\t\tPepperoni for Small pizza: +$2 \t\t\n Pepperoni for Medium pizza: $+3" )
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
print ("\t\tExtra Cheese for any size pizza: +$2")
extra_cheese = input("Do you want extra Cheese? Y, N:  ")  

bill = 0;

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 2

print (f"Your final bill is ${bill}")
