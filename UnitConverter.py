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

validNumbers = [1, 2, 3, 4, 5, 6, 7]

while True:

    display_menu()
    
    while True:
        try:
            option = int(input())
            break
        except ValueError:
            print('Invalid input. Please enter a NUMBER between 1 and 7.')

    if(option not in validNumbers):
        print('Invalid number. Please select a number between 1 and 7.')
        continue

    try:
        theNumber = float(input('Enter the number to convert: '))
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        continue

    if(option == 1):
        km = theNumber
        miles = km * 0.621371
        print(f'{km} kilometers is equal to {miles} miles.')

    elif(option == 2):
        miles = theNumber
        km = miles / 0.621371
        print(f'{miles} miles is equal to {km} kilometers.')

    elif(option == 3):
        celsius = theNumber
        fahrenheit = (celsius * 9/5) + 32
        print(f'{celsius}°C is equal to {fahrenheit}°F.')

    elif(option == 4):
        fahrenheit = theNumber
        celsius = (fahrenheit - 32) * 5/9
        print(f'{fahrenheit}°F is equal to {celsius}°C.')

    elif(option == 5):
        kg = theNumber
        pounds = kg * 2.20462
        print(f'{kg} kilograms is equal to {pounds} pounds.')

    elif(option == 6):
        pounds = theNumber
        kg = pounds / 2.20462
        print(f'{pounds} pounds is equal to {kg} kilograms.')

    elif(option == 7):
        print('Exiting the program. Goodbye!')
        break
