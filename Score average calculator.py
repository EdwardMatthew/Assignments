# Python program to calculate class average score

# Function to input the scores
student1 = eval(input("Enter student1 score here:"))
student2 = eval(input("Enter student2 score here:"))
student3 = eval(input("Enter student3 score here:"))
total_score = student1 + student2 + student3

# Function to calculate the average
average = total_score / 3

#Driver core
print("Student scores:")
print(student1)
print(student2)
print(student3)
print("Averages:", average)
