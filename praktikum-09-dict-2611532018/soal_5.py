n = int(input())

totals = {}  

for _ in range(n):
    nama, nominal = input().split()
    totals[nama] = totals.get(nama, 0) + int(nominal)

for nama, total in totals.items():
    print(f"{nama}: {total}")

print(f"Total cash: {sum(totals.values())}")

top_name = None
top_total = -1
for nama, total in totals.items():
    if total > top_total:   
        top_name = nama
        top_total = total

print(f"Top contributor: {top_name} ({top_total})")