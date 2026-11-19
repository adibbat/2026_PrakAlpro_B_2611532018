LAST_DIGIT = 8  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Input 7 pengeluaran
for day in range(1, 8):
    expense = int(input(f"Day {day}: "))
    expenses.append(expense)

# Menghitung total
total = 0
for expense in expenses:
    total += expense

# Menghitung rata-rata
average = total / 7

# Mencari pengeluaran tertinggi
highest = expenses[0]
highest_day = 1

for i in range(1, 7):
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

# Menghitung hari di atas batas
above_limit = 0
for expense in expenses:
    if expense > daily_limit:
        above_limit += 1

# Menampilkan hasil
print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {above_limit}")