# Python program to calculate the groups and leftover children

# Function to create groups
class1 = 32
class2 = 45
class3 = 51
group1 = class1 // 5
group2 = class2 // 7
group3 = class3 // 6

# Function to find the leftovers student
leftover1 = class1 % 5
leftover2 = class2 % 7
leftover3 = class3 % 6

#Driver core
print("Number of students in each group:")
print("Class 1:", class1)
print("Class 2:", class2)
print("Class 3:", class3)
print("\n")
print("Number of students leftover:")
print("Class 1:", leftover1)
print("Class 2:", leftover2)
print("Class 3:", leftover3)