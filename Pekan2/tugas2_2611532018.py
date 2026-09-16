from typing import Final

BATAS_LULUS: Final[float] = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_2018 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2018 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2018 = int(input("Masukkan Umur : "))
nilai_2018 = float(input("Masukkan Skor Tes Awal : "))

alamat_2018 = """Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

token_2018 = 100 + 3j

lulus_2018 = nilai_2018 >= BATAS_LULUS

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama_2018,
      "| Tipe:", type(nama_2018))

print("Jenis Kelamin :", jenis_kelamin_2018,
      "| Tipe:", type(jenis_kelamin_2018))

print("Alamat Domisili:")
print(alamat_2018,
      "| Tipe:", type(alamat_2018))

print("Umur :", umur_2018, "tahun",
      "| Tipe:", type(umur_2018))

print("Skor Tes Awal :", nilai_2018,
      "| Tipe:", type(nilai_2018))

print("ID Token Sinyal:", token_2018,
      "| Tipe:", type(token_2018))

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print("Batas Minimum Nilai:", BATAS_LULUS)

print("Apakah Dinyatakan Lulus?:", lulus_2018,
      "| Tipe:", type(lulus_2018))