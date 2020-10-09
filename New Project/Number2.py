# planetary weight calculator
def calc_weight(earth_weight, surface_gravity = 23.1):
    mass_on_earth = earth_weight / 9.8
    return mass_on_earth * surface_gravity

print(calc_weight(120, 9.8))
print(calc_weight(120))
print(calc_weight(120, 23.1))






