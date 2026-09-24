# Buat  file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_2018 = float(input("Masukkan total belanja (Rp): "))

# input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2018 = input("Apakah Anda Member? (y/t): ").strip().lower()
is_member_2018 = input_member_2018 in ["y", "ya"]

# input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2018 = input("Apakah kode promo valid? (y/t): ").strip().lower()
is_promo_2018 = input_promo_2018 in ["y", "ya"]

total_diskon_persen_2018 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumbuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_2018 > 1000000:
    total_diskon_persen_2018 += 10 # Diskon belanja besar

if is_member_2018:
    total_diskon_persen_2018 += 5 # Diskon member

if is_promo_2018:
    total_diskon_persen_2018 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2018 = total_belanja_2018 * (total_diskon_persen_2018 / 100)
total_bayar_2018 = total_belanja_2018 - nominal_diskon_2018

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_2018}% (Rp {nominal_diskon_2018:,.0f})")
print(f"Total Bayar    : Rp {total_bayar_2018:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2018}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid