def document_it(func):
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_function

def add_ints(a, b):
    return a + b
explain = document_it(add_ints) # manual
explain(3, 5)
print()

@document_it
def subtract_ints(a, b):
    return a - b
subtract_ints(3,5) # auto (line17)