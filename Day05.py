# divtionary comprehension
univ = "inha university"
count_alphabet1 = {letter: univ.count(letter) for letter in univ}
print(count_alphabet1)

# for loop
univ = "inha university"
count_alphabet2 = {}
for letter in univ:
    count_alphabet2[letter] = univ.count(letter)
print(count_alphabet2)