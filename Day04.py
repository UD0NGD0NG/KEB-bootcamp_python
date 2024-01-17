# make tuple method
t1 = () # empty tuple
t2 = 3,
t3 = 'apple', 'banana', 'car'
subjects = ['Python', 'C++', 'Linux']
t4 = tuple(subjects)
print(type(t1), type(t2), type(t3), type(t4))

a, b, c = t3 # unpacking
print(a, b, c)

tt1 = (8, 3)
tt2 = (7, 3, 4)
tt3 = (7, 3, 5)
print(tt1 < tt2) # False
print(tt2 < tt3) # True

tt4 = tt1 + tt2
tt5 = tt2 + tt1
print(tt4) # (8, 3, 7, 3, 4)
print(tt5) # (7, 3, 4, 8, 3)