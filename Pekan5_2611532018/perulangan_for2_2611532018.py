# Buat  file dengan nama perulangan_for2_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2018 = int(input("Masukkan jumlah perulangan: "))

print("Perulangan ke-0 sampai ke-", ulang_2018-1)
for i_2018 in range(ulang_2018):
    print(i_2018, end=" ")
print()

print("Perulangan ke-1 sampai ke-", ulang_2018)
for i_2018 in range(1, ulang_2018+1):
    print(i_2018, end=" ")