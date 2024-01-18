#help(isPrime)  # print line3~line7
def isPrime(n) -> bool:
    """
    Checks if a number is prime or not
    :param n: parameter to check
    :return: if Prime return True, else return False
    """
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
    return True

l = []
menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) isPrime(single)   4) isPrime(range)   5) Quit program : ")
l.append(menu)
for x in l:
    if x == '1':
        fahrenheit = float(input('Input Fahrenheit : '))
        print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5.0 / 9.0):.4f}C')
    elif x == '2':
        celsius = float(input('Input Celsius : '))
        print(f'Celsius : {celsius}C, Fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')
    elif x == '3':
        number = int(input("Input number : "))
        if isPrime(number):
            print(f'{number} is prime number')
        else:
            print(f'{number} is NOT prime number')
    elif x == '4':
        numbers = input("Enter start number && finish number: ").split()
        n1 = int(numbers[0])
        n2 = int(numbers[1])
        if n1 > n2:
            n1, n2 = n2, n1
        for number in range(n1, n2 + 1):
            if isPrime(number):
                print(number, end=' ')
        print()
    elif x == '5':
        print('Terminate Program.')
        break
    else:
        print('Invalid Input')
    menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) isPrime(single)   4) isPrime(range)   5) Quit program : ")
    l.append(menu)