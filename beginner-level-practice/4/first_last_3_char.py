s = "wonderful"
num_chars = 3
if len(s) < num_chars * 2:
    print("")
else:
    new_string = s[:num_chars] + s[len(s) - num_chars :]
    print(new_string)
