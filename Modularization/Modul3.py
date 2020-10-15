import calendar
def time_of_the_year(a, b, c, d):
    tc = calendar.month(a, b, c, d)
    return tc
print(time_of_the_year(2020, 2, 1, 1))
