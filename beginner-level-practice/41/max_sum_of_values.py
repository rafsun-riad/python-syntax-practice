my_dict = {
    "a": [1, 2, 3],
    "b": [4, 0, -4],
    "c": [3, 5, 9],
    "d": [45, 12, 100],
}

list_sum = []

for values in my_dict.values():
    list_sum.append(sum(values))

print(max(list_sum))
