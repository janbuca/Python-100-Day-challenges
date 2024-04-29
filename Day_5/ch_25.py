# Average Height Exercise
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n]);
print(student_heights);
print(("The Sum of all Student height is ") + str( sum(student_heights)));
print(("Total Student is ") + str( len(student_heights)));
print(int (sum(student_heights) / len(student_heights)))

 
