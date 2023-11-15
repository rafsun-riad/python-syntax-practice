s = "Hello World"
new_s = ""

word_list = s.split(" ")

for word in word_list:
    lowercase_word = word.lower()
    sorted_word = "".join(sorted(lowercase_word))
    new_s += sorted_word + " "

new_s = new_s.rstrip()

print(new_s)
