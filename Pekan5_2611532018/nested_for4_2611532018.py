# Buat  file dengan nama nested_for4_nim.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2018 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2018 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2018 = tinggi_2018
    c_2018 = a_2018
    lebar_2018 = (2 * tinggi_2018) - 2

    for i_2018 in range(1, tinggi_2018 + 1):
        b_2018 = c_2018 + 1

        for j_2018 in range(1, lebar_2018 + 1):

        #Baris atas dan bawah
            if i_2018 == 1 or i_2018 == tinggi_2018:
                if j_2018 == 1 or j_2018 == lebar_2018:
                    print("#", end="")
                else:
                    print("=", end="")

        #Baris isi
            else:
                if j_2018 == 1 or j_2018 == lebar_2018:
                    print("|", end="")
                else:
                    if j_2018 == c_2018:
                        print("<", end="")
                    elif j_2018 == b_2018:
                        print(">", end="")
                    elif j_2018 == (lebar_2018 - c_2018):
                        print("<", end="")
                    elif j_2018 == (lebar_2018 - c_2018 + 1):
                        print(">", end="")
                    elif j_2018 > b_2018 and j_2018 < (lebar_2018 - c_2018):
                        print(".", end="")
                    else:
                        print(" ", end="")

            print()

            #Logika asli java
            a_2018 -= 2

            if a_2018 <= 0:
                c_2018 = (-a_2018) + 2
            else:
                c_2018 = a_2018