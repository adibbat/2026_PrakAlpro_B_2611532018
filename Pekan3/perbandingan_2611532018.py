# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambahkan 4 digit nim terakhir contoh: angka1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversikan menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2018 = int(input("Input angka-1: "))
angka2_2018 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2018 = angka1_2018 > angka2_2018
print("\nOperator Lebih Besar Dari")
print("angka1 > angka2 =", hasil_2018)

# Lebih kecil dari
hasil_2018 = angka1_2018 < angka2_2018
print("\nOperator Lebih Kecil Dari")
print("angka1 < angka2 =", hasil_2018)

# Lebih besar dari atau sama dengan
hasil_2018 = angka1_2018 >= angka2_2018
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil_2018)

# Lebih kecil dari atau sama dengan
hasil_2018 = angka1_2018 <= angka2_2018
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil_2018)

# Sama dengan
hasil_2018 = angka1_2018 == angka2_2018
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil_2018)

# Tidak sama dengan
hasil_2018 = angka1_2018 != angka2_2018
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =", hasil_2018)

# Tambahan: perbandingan berantai
hasil_2018 = 0 < angka1_2018 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil_2018)

hasil_2018 = 0 < angka2_2018 < 100
print("0 < angka2 < 100 =", hasil_2018)