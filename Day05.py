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

numbers = input("Enter number1 && number2 : ").split()
n1 = int(numbers[0])
n2 = int(numbers[1])
if (n1 > n2):
    n1, n2 = n2, n1
for number in range(n1, n2 + 1):
    if isPrime(number):
        print(number, end=' ')