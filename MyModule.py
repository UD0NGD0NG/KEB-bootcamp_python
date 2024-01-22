def isprime(n) -> bool:
    if n < 2:
        return False
    else:
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            i += 1
        return True


def fahrenheit_to_celsius(fahrenheit) -> float:
    return (fahrenheit - 32.0) * 5.0 / 9.0


def celsius_to_fahrenheit(celsius) -> float:
    return (celsius * 9.0 / 5.0) + 32.0