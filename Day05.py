# make set method
s1 = set()
s2 = {1, 5, 4, 2, 3} # unordered
s3 = {'c', 'b', 'a', 'a'} # {'b', 'c', 'a'}  no duplication

# Modify
s2.add(6) # {1, 2, 3, 4, 5, 6}
s2.remove(1) # {2, 3, 4, 5, 6}

# Combination
Prime = {2, 3, 5, 7}
Even = {2, 4, 6, 8}
Odd = {1, 3, 5, 7, 9}
  # 교집합
ss1 = Prime & Odd # {3, 5, 7}
ss2 = Prime.intersection(Even) # {2}
  # 합집합
ss3 = Odd | Even # {1, 2, 3, 4, 5, 6, 7, 8, 9}
ss4 = Even.union(Odd) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
  # 차집합
ss5 = Prime - Odd # {2}
ss6 = Prime.difference(Even) # {3, 5, 7}

# set comprehension
sss1 = {num1 for num1 in range(1, 11)} # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sss2 = {num2 for num2 in range(1, 11) if num2 % 2 == 0} # {2, 4, 6, 8, 10}

# frozen set
ssss1 = frozenset({1, 2, 3}) # immutable
#ssss1.add(5)  # Error