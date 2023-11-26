num_rows = int(input("Enter the number of rows: "))

k = (2 * num_rows) - 2

for i in range(0, num_rows):
    for j in range(0, k):
        print(" ", end="")

    k -= 2

    for j in range(0, i + 1):
        print("*", end=" ")

    print("")
