# Adding Evens Exercise
# You are going to write a program that calculates the sum of all the even number from 1 to 100 include 1 & 100
# e.g 2+4+6+8+10...............+98+100
# total = 0;
# for number in range(2, 101, 2):
#     print(number)
#     total += number
#     print(total)

# In another way

total2 = 0;
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
        print (total2)
