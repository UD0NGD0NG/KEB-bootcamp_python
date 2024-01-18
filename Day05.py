#lambda value: set value code)
z = lambda x: x ** 2  # assign address
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(z, l))) # using lambda's address

print(list(map(lambda y: y ** 3, l))) # using lambda