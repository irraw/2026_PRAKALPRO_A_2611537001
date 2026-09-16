#tugas3_7001
#program ini menggunakan fungsi input()
#program input

# ============================================================
# TUGAS PEKAN 3 - PRAKTIKUM ALGORITMA DAN PEMROGRAMAN
# Materi: Operator Python
# ============================================================

print("=== SISTEM TRANSAKSI TOKO ===")

# ============================================================
# INPUT DATA PELANGGAN
# ============================================================

nama_7001 = input("Masukkan Nama Pelanggan : ")
status_7001 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_7001 = int(input("Masukkan Total Belanja : "))
jumlah_barang_7001 = int(input("Masukkan Jumlah Barang : "))
kode_promo_7001 = input("Masukkan Kode Promo : ").upper()

# ============================================================
# DATA PROMO
# Operator Membership: in dan not in
# ============================================================

daftar_promo_7001 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_7001 = kode_promo_7001 in daftar_promo_7001
promo_tidak_tersedia_7001 = kode_promo_7001 not in daftar_promo_7001

# ============================================================
# OPERATOR PERBANDINGAN
# ============================================================

syarat_belanja_7001 = total_belanja_7001 >= 200000
syarat_barang_7001 = jumlah_barang_7001 >= 3
status_member_7001 = status_7001 == "member"

# ============================================================
# OPERATOR LOGIKA
# ============================================================

# Operator AND
diskon_member_7001 = status_member_7001 and syarat_belanja_7001

# Operator OR
promo_7001 = promo_tersedia_7001 and (syarat_barang_7001 or status_member_7001)

# Operator NOT
bukan_member_7001 = not status_member_7001

# ============================================================
# OPERATOR ARITMATIKA
# ============================================================

# Jika memenuhi syarat diskon member, mendapat diskon 10%
if diskon_member_7001:
    diskon_7001 = total_belanja_7001 * 10 / 100
else:
    diskon_7001 = 0

# Operator pengurangan
total_pembayaran_7001 = total_belanja_7001 - diskon_7001

# Operator pembagian
rata_rata_barang_7001 = total_belanja_7001 / jumlah_barang_7001

# Operator modulus (%)
sisa_pembagian_7001 = total_belanja_7001 % jumlah_barang_7001

# ============================================================
# OPERATOR PENUGASAN
# ============================================================

# Operator +=
poin_7001 = 0
poin_7001 += jumlah_barang_7001

# Operator -=
saldo_poin_7001 = poin_7001
saldo_poin_7001 -= 1

# ============================================================
# OPERATOR IDENTITY
# ============================================================

objek_a_7001 = None
objek_b_7001 = None

hasil_is_7001 = objek_a_7001 is objek_b_7001
hasil_is_not_7001 = objek_a_7001 is not objek_b_7001

# ============================================================
# OPERATOR BITWISE
# ============================================================

# Nilai bit setiap kondisi:
# 0001 = Member
# 0010 = Belanja >= Rp200.000
# 0100 = Jumlah barang >= 3
# 1000 = Kode promo tersedia

kode_status_7001 = 0

if status_member_7001:
    kode_status_7001 = kode_status_7001 | 1

if syarat_belanja_7001:
    kode_status_7001 = kode_status_7001 | 2

if syarat_barang_7001:
    kode_status_7001 = kode_status_7001 | 4

if promo_tersedia_7001:
    kode_status_7001 = kode_status_7001 | 8

# Operator AND (&)
cek_member_bit_7001 = kode_status_7001 & 1
cek_belanja_bit_7001 = kode_status_7001 & 2
cek_barang_bit_7001 = kode_status_7001 & 4
cek_promo_bit_7001 = kode_status_7001 & 8

# Operator XOR (^)
kode_referensi_7001 = 11
perbandingan_status_7001 = kode_status_7001 ^ kode_referensi_7001

# Operator Shift (tambahan)
hasil_shift_7001 = kode_status_7001 << 1

# ============================================================
# HAK AKSES PELANGGAN
# ============================================================

member_access_7001 = cek_member_bit_7001 == 1
promo_access_7001 = cek_promo_bit_7001 == 8
free_shipping_access_7001 = promo_tersedia_7001 and kode_promo_7001 == "GRATISONGKIR"

# ============================================================
# OUTPUT DATA PELANGGAN
# ============================================================

print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_7001)
print("Status Pelanggan     :", status_7001)
print("Total Belanja        : Rp", total_belanja_7001)
print("Jumlah Barang        :", jumlah_barang_7001)
print("Kode Promo           :", kode_promo_7001)

# ============================================================
# OUTPUT HASIL VALIDASI
# ============================================================

print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000       :", syarat_belanja_7001)
print("Jumlah Barang >= 3        :", syarat_barang_7001)
print("Status Member             :", status_member_7001)
print("Kode Promo Tersedia       :", promo_tersedia_7001)
print("Kode Promo Tidak Tersedia :", promo_tidak_tersedia_7001)
print("Mendapatkan Diskon Member :", diskon_member_7001)
print("Mendapatkan Promo         :", promo_7001)

# ============================================================
# OUTPUT HASIL PERHITUNGAN
# ============================================================

print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon       : Rp", diskon_7001)
print("Total Pembayaran      : Rp", total_pembayaran_7001)
print("Rata-rata Harga Barang: Rp", rata_rata_barang_7001)
print("Sisa Pembagian        :", sisa_pembagian_7001)

# ============================================================
# OUTPUT HAK AKSES
# ============================================================

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses        :", kode_status_7001)
print("Member Access         :", member_access_7001)
print("Promo Access          :", promo_access_7001)
print("Free Shipping Access  :", free_shipping_access_7001)

# ============================================================
# OUTPUT OPERATOR ARITMATIKA
# ============================================================

print("\n=== OPERATOR ARITMATIKA ===")
print("Total Belanja - Diskon :", total_belanja_7001, "-", diskon_7001,
      "=", total_pembayaran_7001)
print("Total Belanja / Jumlah :", total_belanja_7001, "/",
      jumlah_barang_7001, "=", rata_rata_barang_7001)
print("Total Belanja % Jumlah :", total_belanja_7001, "%",
      jumlah_barang_7001, "=", sisa_pembagian_7001)

# ============================================================
# OUTPUT OPERATOR PERBANDINGAN
# ============================================================

print("\n=== OPERATOR PERBANDINGAN ===")
print("Total belanja >= 200000 :", total_belanja_7001 >= 200000)
print("Jumlah barang >= 3      :", jumlah_barang_7001 >= 3)
print("Status == member        :", status_7001 == "member")
print("Status != nonmember     :", status_7001 != "nonmember")

# ============================================================
# OUTPUT OPERATOR LOGIKA
# ============================================================

print("\n=== OPERATOR LOGIKA ===")
print("Member AND Belanja >= 200000 :", status_member_7001 and syarat_belanja_7001)
print("Member OR Barang >= 3         :", status_member_7001 or syarat_barang_7001)
print("NOT Member                    :", not status_member_7001)

# ============================================================
# OUTPUT OPERATOR PENUGASAN
# ============================================================

print("\n=== OPERATOR PENUGASAN ===")
print("Poin setelah += jumlah barang :", poin_7001)
print("Saldo poin setelah -= 1       :", saldo_poin_7001)

# ============================================================
# OUTPUT OPERATOR MEMBERSHIP
# ============================================================

print("\n=== OPERATOR KEANGGOTAAN ===")
print("Kode promo menggunakan IN     :", promo_tersedia_7001)
print("Kode promo menggunakan NOT IN :", promo_tidak_tersedia_7001)

# ============================================================
# OUTPUT OPERATOR IDENTITY
# ============================================================

print("\n=== OPERATOR IDENTITAS ===")
print("objek_a is objek_b     :", hasil_is_7001)
print("objek_a is not objek_b :", hasil_is_not_7001)
print("Catatan: is/is not membandingkan identitas objek,")
print("sedangkan == membandingkan nilai/isi objek.")

# ============================================================
# OUTPUT OPERATOR BITWISE
# ============================================================

print("\n=== OPERASI BITWISE ===")
print("=== KODE STATUS TRANSAKSI ===")

print("0001 = Member")
print("0010 = Belanja >= Rp200000")
print("0100 = Jumlah Barang >= 3")
print("1000 = Kode Promo Tersedia")

print("\nKode Biner   :", format(kode_status_7001, "04b"))
print("Kode Desimal :", kode_status_7001)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_7001, "04b"), "& 0001")
print("Hasil Biner   :", format(cek_member_bit_7001, "04b"))
print("Hasil Desimal :", cek_member_bit_7001)

print("\nCek Belanja")
print(format(kode_status_7001, "04b"), "& 0010")
print("Hasil Biner   :", format(cek_belanja_bit_7001, "04b"))
print("Hasil Desimal :", cek_belanja_bit_7001)

print("\nCek Jumlah Barang")
print(format(kode_status_7001, "04b"), "& 0100")
print("Hasil Biner   :", format(cek_barang_bit_7001, "04b"))
print("Hasil Desimal :", cek_barang_bit_7001)

print("\nCek Promo")
print(format(kode_status_7001, "04b"), "& 1000")
print("Hasil Biner   :", format(cek_promo_bit_7001, "04b"))
print("Hasil Desimal :", cek_promo_bit_7001)

print("\n=== PERBANDINGAN STATUS ===")
print("Kode Transaksi :", format(kode_status_7001, "04b"))
print("Kode Referensi :", format(kode_referensi_7001, "04b"))
print(format(kode_status_7001, "04b"), "^",
      format(kode_referensi_7001, "04b"))
print("Hasil Biner   :", format(perbandingan_status_7001, "04b"))
print("Hasil Desimal :", perbandingan_status_7001)

print("\n=== SHIFT ===")
print(format(kode_status_7001, "04b"), "<< 1")
print("Hasil Biner   :", format(hasil_shift_7001, "b"))
print("Hasil Desimal :", hasil_shift_7001)

print("\n=== SELESAI ===")