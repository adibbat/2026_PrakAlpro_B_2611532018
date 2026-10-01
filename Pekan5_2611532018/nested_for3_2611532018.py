# Buat  file dengan nama nested_for3_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2018 = int(input("Masukkan nilai batas: "))
for i_2018 in range(batas_2018 + 1):
    for j_2018 in range(batas_2018+1):
        print(i_2018+j_2018, end=" ")
print()  