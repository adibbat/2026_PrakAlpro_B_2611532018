# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambahkan 4 digit nim terakhir contoh: angka1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversikan menjadi tipe data integer

angka1_2018 = int(input("Input angka-1: "))
angka2_2018 = int(input("Input angka-2: "))

# Penjumlahan 
hasil_2018 = angka1_2018 + angka2_2018
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2018)

# Pengurangan
hasil_2018 = angka1_2018 - angka2_2018
print("\nOperator Pengurangan")
print("Hasil =", hasil_2018)

# Perkalian
hasil_2018 = angka1_2018 * angka2_2018
print("\nOperator Perkalian")
print("Hasil =", hasil_2018)

# Pembagian
if angka2_2018 != 0:
    hasil_2018 = angka1_2018 / angka2_2018
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2018)

    hasil_2018 = angka1_2018 // angka2_2018
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2018)

    hasil_2018 = angka1_2018 % angka2_2018
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2018)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil_2018 = angka1_2018 ** angka2_2018
print("\nOperator Pangkat")
print("Hasil =", hasil_2018)