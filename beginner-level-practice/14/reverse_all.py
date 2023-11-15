s = "Hello World"
new_s = ""

word_list = s.split(" ")

for word in word_list:
    reverse_word = word[::-1]
    swapped_case = reverse_word.swapcase()
    new_s += swapped_case + " "

new_s = new_s.rstrip()

print(new_s)
