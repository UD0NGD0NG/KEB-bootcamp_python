# make list method
l1 = []
l2 = [1, 2, 3]
l3 = list() # empty list
l4 = list('cat') # ['c', 'a', 't']
today = "2024/01/07"
l5 = today.split('/') # ['2024', '01', '07']

#Reverse
ll1 = [1, 2, 3, 4, 5]
ll1.reverse() # Function, No return value
print(ll1)
ll2 = ll1[::-1] # Slicing, Return value
print(ll2)

#Add
subjects = ['Python']
subjects.append('Linux') # ['Python', 'Linux']
subjects.insert(1, 'C++') # ['Python', 'C++', 'Linux']
ssuubbjjeeccttss = subjects * 2 # ['Python', 'C++', 'Linux', 'Python', 'C++', 'Linux']
subject1 = ['Datastructure']
subject2 = ['Algorithm']
subjects.extend(subject1) # ['Python', 'C++', 'Linux', 'Datastructure']
subjects += subject2 # ['Python', 'C++', 'Linux', 'Datastructure', 'Algorithm']
subjects.append(2) # Other type can append

#Delete
del subjects[5]
subjects.remove('Datastructure') # If there are multiple values, only the first item is deleted.
subjects.pop() # pop(0): delete Head, pop(), pop(-1): delete Tail, pop(idx): delete idx
subjects.clear() # delete All