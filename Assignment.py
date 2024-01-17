#1
e2f = dict(dog='chien', cat='chat', walrus='morse')

#2
print(e2f.get('walrus'))

#3
f2e = {}
for value in e2f.items():
    f2e[value[1]] = value[0]

#4
for value in e2f.items():
    if value[1] == 'chien':
        print(value[0])

#5
print(e2f.keys())

#6
life = {
    'animals': {'cats':'Henri', 'octopi':'Grumpy', 'emus':'Lucy'},
    'plants': {},
    'other': {}
}

#7
print(life.keys())

#8
print(life['animals'].keys())

#9
print(life['animals']['cats'])

#10
squares = {key: key * key for key in range(10)}