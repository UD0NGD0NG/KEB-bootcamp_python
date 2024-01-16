number = int(input("Input number : "))
isPrime = True
i = 2
while  i < number:
    if number % i == 0:
        isPrime = False
        break
    i = i + 1

if isPrime:
    print(f'{number} is prime number')
else:
    print(f'{number} is NOT prime number')