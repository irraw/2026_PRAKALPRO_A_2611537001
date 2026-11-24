number_of_rows = 4
seats_per_row = 5

seats = []
for i in range(number_of_rows):
    row = []
    for j in range(seats_per_row):
        row.append(".")
    seats.append(row)


def show_seats():
    for i in range(number_of_rows):
        print(f"Row {i + 1}: " + " ".join(seats[i]))


show_seats()

while True:
    r = int(input("Row (0 to stop): "))
    if r == 0:
        break
    s = int(input("Seat: "))

    if r < 1 or r > number_of_rows or s < 1 or s > seats_per_row:
        print("Invalid seat.")
    elif seats[r - 1][s - 1] == "X":
        print("Seat already taken.")
    else:
        seats[r - 1][s - 1] = "X"
        print("Seat booked.")

    show_seats()

taken = 0
for i in range(number_of_rows):
    for j in range(seats_per_row):
        if seats[i][j] == "X":
            taken += 1

print(f"Seats taken: {taken}")