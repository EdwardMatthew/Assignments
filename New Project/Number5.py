# Temp conversion program
# Function to take in inputs
def convert_temp():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit:"))
    celcius = convert_to_celcius(fahrenheit)
    print("The temperature in Fahrenheit is:", fahrenheit)
    print("The temperature in Celcius is", convert_to_celcius(fahrenheit))
    print("The temperature in Kelvin is", convert_to_kelvin(celcius))

# Helper to convert to Celcius
def convert_to_celcius(fahrenheit):
    celcius = 5/9 * (fahrenheit - 32)
    return celcius

# Helper to convert to Kelvin
def convert_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

convert_temp()