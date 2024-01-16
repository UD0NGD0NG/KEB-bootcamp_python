course = "2024 KEB Bootcamp"
print(course.replace('KEB', 'Inha'))
print(course)
course = course.replace('KEB', 'Inha')
print(course)

str = "a djs aa sf a fad"
print(str.replace('a', 'A')) # All
str = str.replace('a', 'A', 4) # limit
print(str)

world = "!!!!!earth!!!!!earth!!!!!"
print(world)
print(world.strip('!')) # default delimeter is ' '(ws)
print(world.rstrip('!'))
print(world.lstrip('!'))
print(world.find('earth')) # if value is exist find == index
print(world.rindex('earth'))
print(world.find('?')) # if value is not exist return -1
#print(world.index('?'))  # Error!