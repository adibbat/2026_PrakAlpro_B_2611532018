schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

hari_tersibuk = ""
jumlah_terbanyak = -1
for hari, daftar_matkul in schedule.items():
    if len(daftar_matkul) > jumlah_terbanyak:   
        hari_tersibuk = hari
        jumlah_terbanyak = len(daftar_matkul)

print(f"Busiest day: {hari_tersibuk} ({jumlah_terbanyak} courses).")

matkul = input()
jumlah_hari = 0
for hari, daftar_matkul in schedule.items():
    if matkul in daftar_matkul:
        jumlah_hari += 1

print(f"{matkul}: {jumlah_hari} days.")