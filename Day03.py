course = "2024 KEB Bootcamp"
print(course)
list_course = course.split() # default delimeter is ' '(white space)
list_courseB = course.split('B') # set delimeter
print(list_course)
print(list_courseB)

numbers = input("FirstNumber SecondNumber : ").split()
print(numbers[0] + numbers[1]) # concatenation
print(int(numbers[0]) + int(numbers[1])) # arithmetic operation

subjects = ["Python", "C++", "Database"]
subjects_string = '/'.join(subjects)
print(subjects_string)