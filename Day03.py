numbers = input("Input start number finish number: ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])

for number in range(n1, n2 + 1):
    isPrime = True
    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break
        if isPrime:
            print(number, end=' ')