def squares(n):
    return n ** 2
def run_function(f, number):
    return f(number)
print(squares(7))
print(run_function(squares, 7))

def run__function(f, *numbers):
    return [f(num) for num in numbers]
print(run__function(squares, 1, 2, 3, 4, 5))