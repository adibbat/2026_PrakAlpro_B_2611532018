# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambahkan 4 digit nim terakhir contoh: angka1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2018 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2018 = [int(angka.strip()) for angka in input_data_2018.split(",")]

nilai_dicari_2018 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2018 = nilai_dicari_2018 in data_2018
print("\nOperator keanggotaan IN")
print(nilai_dicari_2018, "in", data_2018, "=", hasil_2018)

# Operator not in
hasil_not_in_2018 = nilai_dicari_2018 not in data_2018
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2018, "not in", data_2018, "=", hasil_not_in_2018)


print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_2018 = data_2018

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2018 = objek1_2018

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2018 = data_2018.copy()

print("objek1 =", objek1_2018)
print("objek2 =", objek2_2018)
print("objek3 =", objek3_2018)

# Operator is
hasil_is_2018 = objek1_2018 is objek2_2018
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_is_2018)

# Operator is not
hasil_2018 = objek1_2018 is not objek3_2018
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2018)

# Membandingkan identitas dan nilai
print("\nPerbandingkan identitas dan nilai")
print("objek1 is objek3 =", objek1_2018 is objek3_2018)
print("objek1 == objek3 =", objek1_2018 == objek3_2018)