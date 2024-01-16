university = "Inha\nUniversity"
runiversity = r"Inha\nUniversity" # raw string
print(university)
print(runiversity)

# slicing [start : end : step]
print(university[:4]) # slicing
print(university[:-11]) # reverse slicing
print(university[:len(university)]) # len : return number of letters

number1 = input("First number : ")
number2 = input("Second number : ")
print(number1 + number2) # concatenation
print(number1 * 3) # loop
#print(number1 + 3)  # Error!

String = "abcdefghijklmnopqrstuvwxyz"
print(String[0]) # 0-based
print(String[1])
print(String[25])
print(String[-1]) # reverse(1-based)
print(String[-26])

print(String.replace('a','A')) # String is immutable, but Function can change
print(String) # Change by Function is temporary