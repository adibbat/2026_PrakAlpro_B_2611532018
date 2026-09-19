print("=== SISTEM TRANSAKSI TOKO ===")

# Input
nama_2018 = input("Masukkan Nama Pelanggan : ")
status_2018 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2018 = int(input("Masukkan Total Belanja : "))
jumlah_barang_2018 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2018 = input("Masukkan Kode Promo : ").upper()

# Operator Keanggotaan
daftar_promo_2018 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]
kode_promo_tersedia_2018 = kode_promo_2018 in daftar_promo_2018
kode_promo_tidak_tersedia_2018 = kode_promo_2018 not in daftar_promo_2018

# Operator Perbandingan
syarat_belanja_2018 = total_belanja_2018 >= 200000
syarat_jumlah_barang_2018 = jumlah_barang_2018 >= 3
status_member_2018 = status_2018 == "member"

# Operator Logika
diskon_member_2018 = status_member_2018 and syarat_belanja_2018
promo_barang_2018 = syarat_jumlah_barang_2018 and kode_promo_tersedia_2018
free_shipping_2018 = kode_promo_2018 == "GRATISONGKIR"
mendapatkan_promo_2018 = promo_barang_2018 or free_shipping_2018
bukan_member_2018 = not status_member_2018

# Operator Aritmatika
if diskon_member_2018:
    diskon_2018 = total_belanja_2018 * 10 / 100
else:
    diskon_2018 = 0

total_pembayaran_2018 = total_belanja_2018 - diskon_2018

if jumlah_barang_2018 > 0:
    rata_rata_barang_2018 = total_pembayaran_2018 / jumlah_barang_2018
    sisa_pembagian_2018 = int(total_pembayaran_2018) % jumlah_barang_2018
else:
    rata_rata_barang_2018 = 0
    sisa_pembagian_2018 = 0

# Operator Penugasan
poin_2018 = 0

if diskon_member_2018:
    poin_2018 += 10

if mendapatkan_promo_2018:
    poin_2018 += 5

if kode_promo_tidak_tersedia_2018:
    poin_2018 -= 2

if total_belanja_2018 >= 500000:
    poin_2018 *= 2

# Operator Identitas
objek_promo_1_2018 = ["HEMAT10", "HEMAT20"]
objek_promo_2_2018 = ["HEMAT10", "HEMAT20"]
objek_promo_3_2018 = objek_promo_1_2018

identitas_sama_2018 = objek_promo_1_2018 is objek_promo_3_2018
identitas_berbeda_2018 = objek_promo_1_2018 is not objek_promo_2_2018
nilai_sama_2018 = objek_promo_1_2018 == objek_promo_2_2018

# Operator Bitwise
kode_member_2018 = 1
kode_belanja_2018 = 2
kode_barang_2018 = 4
kode_promo_bit_2018 = 8

kode_status_2018 = 0

if status_member_2018:
    kode_status_2018 |= kode_member_2018

if syarat_belanja_2018:
    kode_status_2018 |= kode_belanja_2018

if syarat_jumlah_barang_2018:
    kode_status_2018 |= kode_barang_2018

if kode_promo_tersedia_2018:
    kode_status_2018 |= kode_promo_bit_2018

cek_member_2018 = kode_status_2018 & kode_member_2018
cek_promo_2018 = kode_status_2018 & kode_promo_bit_2018

kode_referensi_2018 = 11
perbedaan_status_2018 = kode_status_2018 ^ kode_referensi_2018
kode_shift_2018 = kode_status_2018 << 1

# Hak Akses Pelanggan
kode_hak_akses_2018 = 0

if status_member_2018:
    kode_hak_akses_2018 += 1

if mendapatkan_promo_2018:
    kode_hak_akses_2018 += 2

member_access_2018 = status_member_2018
promo_access_2018 = mendapatkan_promo_2018
free_shipping_access_2018 = free_shipping_2018

print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan       :", nama_2018)
print("Status Pelanggan     :", status_2018)
print("Total Belanja        : Rp" + str(total_belanja_2018))
print("Jumlah Barang        :", jumlah_barang_2018)
print("Kode Promo           :", kode_promo_2018)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_2018)
print("Jumlah Barang >= 3   :", syarat_jumlah_barang_2018)
print("Status Member        :", status_member_2018)
print("Kode Promo Tersedia  :", kode_promo_tersedia_2018)
print("Mendapatkan Diskon   :", diskon_member_2018)
print("Mendapatkan Promo    :", mendapatkan_promo_2018)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon               : Rp" + str(int(diskon_2018)))
print("Total Pembayaran     : Rp" + str(int(total_pembayaran_2018)))
print("Rata-rata Harga Barang : Rp" + str(int(rata_rata_barang_2018)))

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", kode_hak_akses_2018)
print("Member Access        :", member_access_2018)
print("Promo Access         :", promo_access_2018)
print("Free Shipping Access :", free_shipping_access_2018)

print("\n=== HASIL OPERATOR ===")

print("\nOperator Aritmatika")
print("Diskon = Total Belanja * 10 / 100")
print("Total Pembayaran = Total Belanja - Diskon")
print("Rata-rata = Total Pembayaran / Jumlah Barang")
print("Sisa Pembagian =", sisa_pembagian_2018)

print("\nOperator Perbandingan")
print("Belanja >= 200000 :", syarat_belanja_2018)
print("Jumlah Barang >= 3 :", syarat_jumlah_barang_2018)
print("Status == member :", status_member_2018)

print("\nOperator Logika")
print("Member AND Belanja :", diskon_member_2018)
print("Barang AND Promo   :", promo_barang_2018)
print("Promo OR Gratis Ongkir :", mendapatkan_promo_2018)
print("NOT Member         :", bukan_member_2018)

print("\nOperator Penugasan")
print("Poin Pelanggan     :", poin_2018)
print("Operator digunakan : +=, -=, *=")

print("\nOperator Keanggotaan")
print("Kode Promo in daftar     :", kode_promo_tersedia_2018)
print("Kode Promo not in daftar :", kode_promo_tidak_tersedia_2018)

print("\nOperator Identitas")
print("Objek 1 is Objek 3     :", identitas_sama_2018)
print("Objek 1 is not Objek 2 :", identitas_berbeda_2018)
print("Objek 1 == Objek 2     :", nilai_sama_2018)

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner   :", format(kode_status_2018, "04b"))
print("Kode Desimal :", kode_status_2018)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(format(kode_status_2018, "04b"), "&", format(kode_member_2018, "04b"))
print("Hasil Biner   :", format(cek_member_2018, "04b"))
print("Hasil Desimal :", cek_member_2018)

print("\nCek Promo")
print(format(kode_status_2018, "04b"), "&", format(kode_promo_bit_2018, "04b"))
print("Hasil Biner   :", format(cek_promo_2018, "04b"))
print("Hasil Desimal :", cek_promo_2018)

print("\n=== Perbandingan Status ===")
print("Kode Transaksi :", format(kode_status_2018, "04b"))
print("Kode Referensi :", format(kode_referensi_2018, "04b"))
print(format(kode_status_2018, "04b"), "^", format(kode_referensi_2018, "04b"))
print("Hasil Biner   :", format(perbedaan_status_2018, "04b"))
print("Hasil Desimal :", perbedaan_status_2018)

print("\n=== Shift ===")
print(format(kode_status_2018, "04b"), "<< 1")
print("Hasil Biner   :", format(kode_shift_2018, "b"))
print("Hasil Desimal :", kode_shift_2018)

print("\n=== SELESAI ===")