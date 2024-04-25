# PEMDAS
    # Parentheses    ---> ()
    # Exponents      ---> **
    # Multiplication ---> *
    # Division       ---> /
    # Addition       ---> +
    # Subtraction    ---> -

print(3 * 3 + 3 / 3 - 3);

# Body mass index

# Don't change the code below
height = input("Enter your height in m: ");
weight = input("Enter your weight in kg: ");
# Dont't change the code above

# Print the type of the variable 
print(type(weight))
print(type(height))

# Write your code below this line
height_as_float = float(height);
weight_as_int = int(weight);

# Using the exponent operator **
bmi = (weight_as_int / (height_as_float ** 2));
# Or using multiplication and PEMDAS
bmi = (weight_as_int / (height_as_float * height_as_float));
print(bmi);

# bmi_as_int = int(bmi);
# print(bmi_as_int);