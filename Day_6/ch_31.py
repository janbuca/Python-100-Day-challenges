def my_function():
    print("Hello from a function")

my_function()


# Function that allows for input 
def my_function(fname):
    print(fname + " Refsnes")

my_function("John")
my_function("Tobias")
my_function("Linus")


# Function with default value for an argument 
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Function with variable number of arguments 
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("John", "Tobias", "Linus")


# Function with keyword arguments 
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "John", child2 = "Tobias", child3 = "Linus")


# Arbitrary Keyword Arguments, **kwargs 
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


# Return Values 
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))

print(my_function(9))


# The pass Statement 
# def myfunction():
#     pass 



# Recursion   
def tri_recursion(k): 
    if(k > 0): 
        result = k + tri_recursion(k - 1) 
        print(result) 
#         else:
result = 0
# return result
