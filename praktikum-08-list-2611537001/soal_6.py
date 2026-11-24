LAST_DIGIT = 1
daily_limit =30000 + LAST_DIGIT * 1000
expenses = []
for i in range(1, 8):
    expenses.append(int(input(f"Day {i}: ")))

total = 0
highest = 1
days_above_limit = 0

for i in range(len(expenses)):
    total += expenses[i]
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        days_above_limit += 1

average = total / 7

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {days_above_limit}")