# Buat  file dengan nama jumlah_genap_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2018 = int(input("Masukkan nilai batas: "))

jumlah_2018 = 0
for i_2018 in range(1, ulang_2018 + 1):
    if i_2018 % 2 == 0:
        print(i_2018, end=" ")
        jumlah_2018 = jumlah_2018 + i_2018

        if i_2018 < ulang_2018:
            print(" + ", end=" ")
        else:
            print(" = ", jumlah_2018,end=" ")
print()
print("Jumlah =", jumlah_2018)