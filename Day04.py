l1 = [1, 3, 6, 12, 612, 2]
l2 = sorted(l1) # origin list isn't change
print(l1, l2)
l1.sort() # Asc
l2.sort(reverse=True) # Desc
print(l1, l2)