def isPrime(n):
    if n < 2:
        return False
    else:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
    return True

n1, n2 = map(int, input('Enter begin && end : ').split())
n1, n2 = min(n1, n2), max(n1, n2)
for number in range(n1, n2 + 1):
    if isPrime(number):
        print(number, end=' ')