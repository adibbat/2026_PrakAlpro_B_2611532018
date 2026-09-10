# Buat file dengan nama Boolean_NIM.py
# nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_2018 = True
is_cumlaude_2018 = True

# Menggunakan Boolean
nilai_2018 = 85
batas_lulus_2018 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2018 = nilai_2018 >= batas_lulus_2018 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_2018)
print("Apakah Lulus?:", status_kelulusan_2018)
if is_lulus_2018 and is_cumlaude_2018:
    print("Selamat, Anda Lulus dengan Predikat Cum Laude!")
