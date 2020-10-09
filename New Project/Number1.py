# Main Function
def convert_to_days():
    hours = float(input("Enter number of hours:"))
    minutes = float(input("Enter number of minutes:"))
    seconds = float(input("Enter number of seconds:"))
    print("The number of days is:", get_days(hours, minutes, seconds))

# Helper Function
def get_days(hours, minutes, seconds):
    days = (hours / 24) + (minutes / (24 * 60)) + (seconds / (24 * 3600))
    days_final = round(days, 4)
    return days_final

convert_to_days()