#Tugas 5 
#Pola Jam Pasir Kristal Palindromik Berbingkai (Framed Palindromic Crystal Hourglass)

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_2018 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai atas
print("#", end="")
for garis_2018 in range(4 * n_2018 + 5):
    print("=", end="")
print("#")

# Fase 1
for baris_2018 in range(n_2018, 0, -1):
    print("|", end="")
    print(" ", end="")                              
    for spasi_2018 in range(2 * (n_2018 - baris_2018)):
        print(" ", end="")                          
    for angka_2018 in range(baris_2018, 0, -1):
        print(angka_2018, end=" ")                  
    print("<*>", end="")                            
    for angka_2018 in range(1, baris_2018 + 1):
        print(" ", end="")
        print(angka_2018, end="")                  
    for spasi_2018 in range(2 * (n_2018 - baris_2018)):
        print(" ", end="")                         
    print(" ", end="")                          
    print("|")

# Fase 2
print("|", end="")
for spasi_2018 in range(2 * n_2018 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_2018 in range(2 * n_2018 + 1):
    print(" ", end="")
print("|")

# Fase 3
for baris_2018 in range(1, n_2018 + 1):
    print("|", end="")
    print(" ", end="")
    for spasi_2018 in range(2 * (n_2018 - baris_2018)):
        print(" ", end="")
    for angka_2018 in range(baris_2018, 0, -1):
        print(angka_2018, end=" ")
    print("<*>", end="")
    for angka_2018 in range(1, baris_2018 + 1):
        print(" ", end="")
        print(angka_2018, end="")
    for spasi_2018 in range(2 * (n_2018 - baris_2018)):
        print(" ", end="")
    print(" ", end="")
    print("|")

# Bingkai bawah
print("#", end="")
for garis_2018 in range(4 * n_2018 + 5):
    print("=", end="")
print("#")