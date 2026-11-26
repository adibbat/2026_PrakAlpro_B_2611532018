mahasiswas = input().split()
pengumpul = input().split()

mahasiswas_set = set(mahasiswas)
pengumpul_set = set(pengumpul)

pengumpul_count = len(pengumpul_set)

ga_ngumpul = mahasiswas_set - pengumpul_set

print(f"Submitted: {pengumpul_count} students")
print(f"Not submitted: {len(ga_ngumpul)} students")

for mahasiswa in mahasiswas:
    if mahasiswa not in pengumpul_set:
        print(mahasiswa)