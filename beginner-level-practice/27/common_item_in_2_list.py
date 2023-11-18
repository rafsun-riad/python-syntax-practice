list_a = [1, 2, 3, 4]
list_b = [1, 2, 3, 4]

common_elem = []

for elem in list_a:
    if elem in list_b:
        common_elem.append(elem)

print(common_elem)
