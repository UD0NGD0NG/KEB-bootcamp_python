class Oops(Exception):
    pass
try:
    print ("Good")
    raise Oops("oops")
except Oops as err:
    print(f"{err}")
except Exception: # catch all error (must be last)
    print("Error occurs")