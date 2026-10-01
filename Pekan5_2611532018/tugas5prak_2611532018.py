#Tugas atau Latihan mungkin?

tinggi_2018 = int(input("Masukkan tinggi segitiga: "))

for i_2018 in range(1, tinggi_2018 + 1):
    print(" " * (tinggi_2018 - i_2018), end="")

    for j_2018 in range(i_2018):
        print("*", end=" ")
    
    print()