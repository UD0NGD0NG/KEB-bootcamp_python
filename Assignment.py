#1
def good():
    return ['Harry', 'Ron', 'Hermione']

#2
def get_odds():
    number = 1
    while number < 10:
        yield number
        number += 2
idx = 1
for num in get_odds():
    if idx == 3:
        print(num)
    idx += 1

#3
def test(func):
    def new_test(*args, **kwargs):
        print("start")
        tmp = func(*args, **kwargs)
        print("end")
        return tmp
    return new_test

@test
def Func():
    print('Test')

Func()

#4
class OopsError(Exception):
    pass
try:
    raise OopsError('Caught an oops')
except OopsError as exc:
    print(exc)