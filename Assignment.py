l = []
menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
l.append(menu)
for x in l:
    if x == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    elif x == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')
    elif x == '3':
        print('Terminate Program.')
        break
    else:
        print('Invalid Input')
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")
    l.append(menu)