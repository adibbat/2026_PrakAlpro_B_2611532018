# Buat  file dengan nama nested_for1_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2018 = int(input("Masukkan nilai batas: "))
for line_2018 in range(1, batas_2018 + 1):
    for j_2018 in range(1, (-1 * line_2018 + batas_2018) + 1):
        print(" . ", end="")
print()  