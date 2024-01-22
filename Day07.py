# import MyModule -1
# from MyModule import * -2
import MyModule as mm # -3

while True:
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Prime1   4) Prime2   5) Quit program : ")

    if menu == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        # print(f'Fahrenheit : {fahrenheit}F, Celsius : {MyModule.fahrenheit_to_celsius(fahrenheit):.4f}C\n') -1
        # print(f'Fahrenheit : {fahrenheit}F, Celsius : {fahrenheit_to_celsius(fahrenheit):.4f}C\n') -2
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {mm.fahrenheit_to_celsius(fahrenheit):.4f}C\n') # -3
    elif menu == '2':
        celsius = float(input('Input Celsius : '))
        # print(f'Celsius : {celsius}C, Fahrenheit : {MyModule.celsius_to_fahrenheit(celsius):.4f}F\n') -1
        # print(f'Celsius : {celsius}C, Fahrenheit : {celsius_to_fahrenheit(celsius):.4f}F\n') -2
        print(f'Celsius : {celsius}C, Fahrenheit : {mm.celsius_to_fahrenheit(celsius):.4f}F\n') # -3
    elif menu == '3':
        number = int(input("Input number : "))
        # if MyModule.isprime(number): -1
        # if isprime(number): -2
        if mm.isprime(number): # -3
            print(f'{number} is prime number\n')
        else:
            print(f'{number} is NOT prime number!\n')
    elif menu == '4':
        numbers = input("Input first second number : ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        if n1 > n2:
            n1, n2 = n2, n1

        for number in range(n1, n2 + 1):
            # if MyModule.isprime(number): -1
            # if isprime(number): -2
            if mm.isprime(number): # -3
                print(number, end=' ')
        print('\n')
    elif menu == '5':
        print('Terminate Program.\n')
        break
    else:
        print('Invalid Menu!\n')