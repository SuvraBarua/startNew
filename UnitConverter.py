from unittest import case


print('== Unit Converter Program==')

def display_menu():
    print('1. Kilometers to Miles')
    print('2. Miles to Kilometers')
    print('3. Celsius to Fahrenheit')
    print('4. Fahrenheit to Celsius')
    print('5. Kilograms to Pounds')
    print('6. Pounds to Kilograms')
    print('7. Exit')

    print('Please select an option (1-7): ')

option = 0
theNumber = 0

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
            print(f'{km:.2f} kilometers is equal to {miles:.2f} miles.')

        case 2:
            miles = theNumber
            km = miles / 0.621371
            print(f'{miles:.2f} miles is equal to {km:.2f} kilometers.')

        case 3:
            celsius = theNumber
            fahrenheit = (celsius * 9/5) + 32
            print(f'{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.')

        case 4:
            fahrenheit = theNumber
            celsius = (fahrenheit - 32) * 5/9
            print(f'{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.')

        case 5:
            kg = theNumber
            pounds = kg * 2.20462
            print(f'{kg:.2f} kilograms is equal to {pounds:.2f} pounds.')

        case 6:
            pounds = theNumber
            kg = pounds / 2.20462
            print(f'{pounds:.2f} pounds is equal to {kg:.2f} kilograms.')
