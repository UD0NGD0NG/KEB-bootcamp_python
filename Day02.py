a = [10, 20, 30, 40, 50]
b = a # 복사가 아닌 참조
print(a, b)
a[0] = 50
print(a, b)
b[0] = 100
print(a, b)

money = 1,000,000 # tuple
print(money)
print(type(money))
cash = 1_000_000
print(cash)
print(type(cash))