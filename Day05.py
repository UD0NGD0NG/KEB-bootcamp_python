def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number # remember just before
        number += step

ranger = my_range(1, 5)

for x in ranger:
    print(x)

for x in ranger: # print nothing
    print(x)

# comprehension
gen_obj = (num for num in range(1, 5))
for x in gen_obj:
    print(x)

for x in gen_obj: # print nothing
    print(x)