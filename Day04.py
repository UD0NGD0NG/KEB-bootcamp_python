# shallow copy
l1 = [1, 2, 3] # Values in list are immutable
l2 = l1
l3 = l1.copy()
l4 = list(l1)
l5 = l1[:]
l1[1] = 20
print(l1, l2, l3, l4, l5)

# deep copy
ll1 = [1, [2, 3], 4] # ll1[1] is mutable
ll2 = ll1
ll3 = ll1.copy()
ll4 = list(ll1)
ll5 = ll1[:]
ll1[1][0] = 20
print(ll1, ll2, ll3, ll4, ll5)