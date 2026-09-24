# Buat  file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2018 = int(input("Inputkan Umur Anda = "))
sim_2018 = input("Apakah Anda sudah punya SIM C (y/t) = ")[0]

if umur_2018 >= 17 and sim_2018 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_2018 >= 17 and sim_2018 != "y":
    print("Anda sudah dewasa tetapi belum boleh bawa motor")

if umur_2018 < 17 and sim_2018 == "y":
    print("Anda belum Cukup Umur punya SIM")

if umur_2018 < 17 and sim_2018 != "y":
    print("Anda belum Cukup Umur bawa motor")
print("Program Selesai")