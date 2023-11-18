list_a = [1, 2, 3, 4]
list_b = [1, 2]

difference = []

for elem in list_a:
    if elem not in list_b:
        difference.append(elem)

print(difference)
