menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below

for d in range(1, number_of_days + 1):
    row = []
    for name in menus:
        row.append(int(input(f"Day {d}, {name}: ")))
    sales.append(row)

print("Total per day:")
for i in range(number_of_days):
    day_total = 0
    for j in range(len(menus)):
        day_total += sales[i][j]
    print(f"Day {i + 1}: {day_total}")

menu_totals = []
for j in range(len(menus)):
    col_total = 0
    for i in range(number_of_days):
        col_total += sales[i][j]
    menu_totals.append((menus[j], col_total))

print("Total per menu:", menu_totals)

best_name = ""
best_total = -1
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")