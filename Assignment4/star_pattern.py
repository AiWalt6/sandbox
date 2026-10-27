ROWS = 7

for row in range(ROWS, 0, -1):
    for column in range(row):
        print("*", end="")
    print()
