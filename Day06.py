def factorial_repetition(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursion(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursion(n - 1)

n = int(input("number : "))
print(factorial_repetition(n))
print(factorial_recursion(n))