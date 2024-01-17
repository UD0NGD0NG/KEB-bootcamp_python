# make dictionary method
d1 = {}
d2 = {'a': 'apple', 'b' : 'banana', 'c': 'cat'}
d3 = dict(A = 'Apple', B = 'Banana', C = 'Cat')
l = [(1, 2), (3, 4), (5, 6)] # list -> dictionary
d4 = dict(l) # {1: 2, 3: 4, 5: 6}
t = ([1, 10], [2, 20], [3, 30]) # tuple -> dictionary
d5 = dict(t) # {1: 10, 2: 20, 3: 30}
ll = ['ab', 'cd', 'ef'] # string(len == 2) list -> dictionary
d6 = dict(ll) # {'a': 'b', 'c': 'd', 'e': 'f'}

Grades = {'Python': 'A+', 'C++': 'A+'}
Grades['Calculus'] = 'A+' # Add
Grades['Calculus'] = 'A0' # Edit
print(Grades.get('Java', "Didn't take a course")) # second string is optional, default is None

print(Grades.keys())
print(Grades.values())
print(Grades.items())

# Combine
dd1 = dict(a='apple', b='banana', c='car')
dd2 = dict(c = 'cat', e = 'elephant')
dd3 = {**dd1, **dd2} # If there are overlapping keys, the value of the dictionary located at the back is stored.
dd1.update(dd2)
print(dd1, dd3)