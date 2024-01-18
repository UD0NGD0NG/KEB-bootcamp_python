# Inner Func
def Out_F(a, b):
    def In_F(c, d):
        return c + d
    return In_F(a, b)
print(Out_F(4, 5))

# Closure
def out_f(a, b):
    def in_f(): # no parameter
        return a + b
    return in_f # return address
clo = out_f(4, 5)
print(clo) # address
print(clo()) # run in_f(a, b)