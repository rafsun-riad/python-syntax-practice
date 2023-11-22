my_list = [["a", 1], ["b", 2], ["c", 3], ["d", 4]]

new_dict = {}

for nested_list in my_list:
    new_dict[nested_list[0]] = nested_list[1]

print(new_dict)
