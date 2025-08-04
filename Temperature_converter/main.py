def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def convert_temperature():
    print("Temperature Converter")
    print("Choose the input scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    choice = input("Enter your choice (1/2/3): ")

    if choice not in ['1', '2', '3']:
        print("Invalid choice.")
        return

    temp = float(input("Enter the temperature value: "))

    if choice == '1':
        print(f"{temp}°C is equal to {celsius_to_fahrenheit(temp):.2f}°F")
        print(f"{temp}°C is equal to {celsius_to_kelvin(temp):.2f}K")
    elif choice == '2':
        print(f"{temp}°F is equal to {fahrenheit_to_celsius(temp):.2f}°C")
        print(f"{temp}°F is equal to {fahrenheit_to_kelvin(temp):.2f}K")
    elif choice == '3':
        print(f"{temp}K is equal to {kelvin_to_celsius(temp):.2f}°C")
        print(f"{temp}K is equal to {kelvin_to_fahrenheit(temp):.2f}°F")

if __name__ == "__main__":
    convert_temperature()
