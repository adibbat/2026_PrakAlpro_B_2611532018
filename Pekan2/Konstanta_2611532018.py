# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2018 = float(input('masukkan nilai jari-jari: '))
luas_2018 = PI * jari_2018 * jari_2018
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2018, luas_2018))