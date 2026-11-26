n = int(input())

totals = {}  # dictionary: nama -> total setoran (urutan kemunculan pertama terjaga)

for _ in range(n):
    nama, nominal = input().split()
    totals[nama] = totals.get(nama, 0) + int(nominal)

# Cetak rekap per mahasiswa
for nama, total in totals.items():
    print(f"{nama}: {total}")

# Total kas
print(f"Total cash: {sum(totals.values())}")

# Penyetor terbesar (jika seri, yang muncul lebih dulu)
top_name = None
top_total = -1
for nama, total in totals.items():
    if total > top_total:   # pakai ">" (bukan ">=") supaya yang lebih dulu menang saat seri
        top_name = nama
        top_total = total

print(f"Top contributor: {top_name} ({top_total})")