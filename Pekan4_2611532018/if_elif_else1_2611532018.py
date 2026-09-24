# Buat  file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2018 = int(input("Inputkan Umur Anda = "))
sim_2018 = input("Apakah Anda sudah punya SIM C (y/t) = ")[0]

if umur_2018 >= 17 and sim_2018 == "y":
    print("Anda sudah dewasa dan boleh bawa motor")
elif umur_2018 >= 17 and sim_2018 != "y":
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_2018 < 17 and sim_2018 == "y":
    print("Anda belum Cukup Umur punya SIM")
else:
    print("Anda belum Cukup Umur dan tidak boleh bawa motor")
print("Program Selesai")