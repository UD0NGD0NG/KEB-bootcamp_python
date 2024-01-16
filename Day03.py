number = int(input("Input number : "))
isPrime = True
if number < 2:
    print(f'{number} is NOT prime number')
else:
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
            break

    if isPrime:
        print(f'{number} is prime number')
    else:
        print(f'{number} is NOT prime number')