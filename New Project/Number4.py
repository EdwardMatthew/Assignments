# Aspect ratio calculator
def calc_new_height():
    width = input("Enter the current width:")
    height = input("Enter the current height:")
    desired_width = input("Enter the desired width:")
    return (float(desired_width) * float(height)) / float(width)

print("The corresponding height is:",calc_new_height())