# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n========================================")
print("3. OPERATOR BITWISE")
print("========================================")

angka1_2018 = int(input("Masukkan angka bitwise-1: "))
angka2_2018 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2018, "| biner =", bin(angka1_2018))
print("angka2 =", angka2_2018, "| biner =", bin(angka2_2018))

# Bitwise AND
hasil = angka1_2018 & angka2_2018
print("\nBitwise AND (&)")
print(angka1_2018, "&", angka2_2018, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_2018 | angka2_2018
print("\nBitwise OR (|)")
print(angka1_2018, "|", angka2_2018, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_2018 ^ angka2_2018
print("\nBitwise XOR (^)")
print(angka1_2018, "^", angka2_2018, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_2018
print("\nBitwise NOT (~)")
print("~", angka1_2018, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_2018 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_2018, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_2018 >> jumlah_geser
print("\nBitwise geser kanan (>>)")
print(angka1_2018, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))