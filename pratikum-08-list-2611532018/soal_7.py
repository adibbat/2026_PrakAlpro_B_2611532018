menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Input data
for day in range(number_of_days):
    daily_sales = []

    for menu in menus:
        amount = int(input(f"Day {day + 1}, {menu}: "))
        daily_sales.append(amount)

    sales.append(daily_sales)

# Total per hari
print("Total per day:")

for day in range(number_of_days):
    total = 0

    for amount in sales[day]:
        total += amount

    print(f"Day {day + 1}: {total}")

# Total per menu
menu_totals = []

for column in range(len(menus)):
    total = 0

    for row in range(number_of_days):
        total += sales[row][column]

    menu_totals.append((menus[column], total))

print("Total per menu:", menu_totals)

# Best seller
best_name = ""
best_total = -1

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")