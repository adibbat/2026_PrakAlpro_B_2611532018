# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambahkan 4 digit nim terakhir contoh: angka1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversikan menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2018 = int(input("Input angka-1: ")) 
angka2_2018 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2018)
print("Nilai angka2 =", angka2_2018)

# Assignment biasa
hasil_2018 = angka1_2018
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2018)

# Assignment penambahan
hasil_2018 = angka1_2018
hasil_2018 += angka2_2018
print("\nAssignment penambahan (+=)")
print("Hasil =")

# Assignment pengurangan
hasil_2018 = angka1_2018
hasil_2018 -= angka2_2018
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2018)

# Assignment perkalian
hasil_2018 = angka1_2018
hasil_2018 *= angka2_2018
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_2018)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2018 != 0:
    hasil_2018 = angka1_2018
    hasil_2018 /= angka2_2018
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2018)
    # Operator tambahan
    hasil_2018 = angka1_2018
    hasil_2018 //= angka2_2018
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2018)
    hasil_2018 = angka1_2018
    hasil_2018 %= angka2_2018
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2018)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("Angka kedua tidak boleh bernilai 0")

# Operator tambahan: assignment perpangkatan
hasil_2018 = angka1_2018
hasil_2018 **= angka2_2018
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2018)