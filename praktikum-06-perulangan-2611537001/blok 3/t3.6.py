for row in range(4, 0 , -1):
    for column in range(4 - row):
        print(" ", end="")
    for column in range(row):
        print("*", end="")
        if column < row - 1:
            print(" ", end="")
    print()