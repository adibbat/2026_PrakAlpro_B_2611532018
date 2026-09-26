print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# input dari pengguna
nama_2018 = input("Masukkan Nama Pengunjung: ")
umur_2018 = int(input("Input umur anda: "))
sim_2018 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()[0]

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

# input dari pengguna
paket_2018 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_2018 = int(input("Masukkan jumlah tiket           : "))

# if tunggal: validasi kelogisan jumlah tiket
if jumlah_tiket_2018 <= 0:
    print("Peringatan: Kuota tiket tidak valid!")

is_member_2018 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_2018 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Pemilihan Wahana Menggunakan Match Case
match paket_2018:
    case 1:
        nama_wahana_2018 = "Wahana Safari Rimba"
        harga_satuan_2018 = 50000
    case 2:
        nama_wahana_2018 = "Wahana Arung Jeram"
        harga_satuan_2018 = 75000
    case 3:
        nama_wahana_2018 = "Wahana Motor ATV Ekstrim"
        harga_satuan_2018 = 120000
    case 4:
        nama_wahana_2018 = "Wahana Roller Coaster Kilat"
        harga_satuan_2018 = 100000
    case 5:
        nama_wahana_2018 = "Wahana All-Access VIP"
        harga_satuan_2018 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# Validasi Izin Kendali Wahana (IF-ELIF-ELSE + AND/!=)
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")

if paket_2018 == 3:
    if umur_2018 >= 17 and sim_2018 == 'y':
        status_akses_2018 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
    elif umur_2018 >= 17 and sim_2018 != 'y':
        status_akses_2018 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
    elif umur_2018 < 17 and sim_2018 == 'y':
        status_akses_2018 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
    else:
        status_akses_2018 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
else:
    if umur_2018 >= 10:
        status_akses_2018 = "Umur memenuhi syarat untuk menaiki wahana ini."
    else:
        status_akses_2018 = "Umur belum memenuhi syarat untuk menaiki wahana ini."

print(f"Status Akses: {status_akses_2018}")

# Diskon bisa ditumbuk (akumulasi) jika memenuhi beberapa syarat sekaligus
subtotal_2018 = harga_satuan_2018 * jumlah_tiket_2018
total_diskon_persen_2018 = 0

if subtotal_2018 >= 200000:
    total_diskon_persen_2018 += 10   

if is_member_2018 in ['y', 'ya']:
    total_diskon_persen_2018 += 5    

if kode_promo_2018 in ['y', 'ya']:
    total_diskon_persen_2018 += 15   

if jumlah_tiket_2018 >= 5:
    total_diskon_persen_2018 += 5    

# Evaluasi Kelulusan Audit (IF-ELSE)
nominal_diskon_2018 = subtotal_2018 * (total_diskon_persen_2018 / 100)
total_bayar_2018 = subtotal_2018 - nominal_diskon_2018

if total_bayar_2018 > 300000:
    catatan_layanan_2018 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2018 = "Terima kasih telah berkunjung."

# Rincian Pembayaran
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_2018:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2018}% (Rp {nominal_diskon_2018:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2018:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2018}")
print("Program Selesai")