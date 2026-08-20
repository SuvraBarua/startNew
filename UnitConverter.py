def display_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')
    print('5. Kilograms to Pounds')
    print('6. Pounds to Kilograms')
    print('7. Exit')

    print('Please select an option (1-7): ')

def print_conversion(value, unit1, result, unit2):
    print(f'{value:.2f} {unit1} is equal to {result:.2f} {unit2}.')

print('== Unit Converter Program==')

option = 0

while True:

    display_menu()
    
    while True:
        try:
            option = int(input())
            break
        except ValueError:
            print('Invalid input. Please enter a NUMBER between 1 and 7.')

    if(option < 1 or option > 7):
        print('Invalid number. Please select a number between 1 and 7.')
        continue

    if(option == 7):
        print('Exiting the program. Goodbye!')
        break

    try:
        theNumber = float(input('Enter the number to convert: '))
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        continue

    match option:
        case 1:
            km = theNumber
            miles = km * 0.621371
            print_conversion(km, "kilometers", miles, "miles")

        case 2:
            miles = theNumber
            km = miles / 0.621371
            print_conversion(miles, "miles", km, "kilometers")

        case 3:
            celsius = theNumber
            fahrenheit = (celsius * 9/5) + 32
            print_conversion(celsius, "°C", fahrenheit, "°F")

        case 4:
            fahrenheit = theNumber
            celsius = (fahrenheit - 32) * 5/9
            print_conversion(fahrenheit, "°F", celsius, "°C")

        case 5:
            kg = theNumber
            pounds = kg * 2.20462
            print_conversion(kg, "kilograms", pounds, "pounds")

        case 6:
            pounds = theNumber
            kg = pounds * 0.453592
            print_conversion(pounds, "pounds", kg, "kilograms")
