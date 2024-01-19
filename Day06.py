import random
numbers = [random.randint(1, 100) for i in range(10)]

try:
    pick = int(input(f"Enter index (0 ~ {len(numbers) - 1}) : "))
    print(numbers[pick])
    print(5 / 0)
except IndexError as err:
    print(f"{err} : Wrong index number")
except ValueError:
    print("Enter only number")
except ZeroDivisionError as err:
    print(f"{err}")
except Exception: # catch all error (must be last)
    print("Error occurs")