# Buat  file dengan nama if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

ipk_2018 = float(input("Inputkan IPK Anda = "))

if ipk_2018 > 2.75:
    print("Anda Lulus Sangat Memuaskan dengan IPK " + str(ipk_2018))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")