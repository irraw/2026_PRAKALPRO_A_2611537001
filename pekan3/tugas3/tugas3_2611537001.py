#tugas3_7001
#program ini menggunakan fungsi input()
#program input

print("=== SISTEM TRANSAKSI TOKO ===")

# INPUT
nama_7001 = input("Nama: ")
status_7001 = input("Masukkan Status Pelanggan (member/nonmember)): ").lower()
total_7001 = float(input("Total belanja: "))
jumlah_7001 = int(input("Jumlah barang: "))
promo_7001 = input("Kode promo: ").upper()

member_7001 = status_7001 == "y"
promo_list_7001 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# MEMBERSHIP
promo_tersedia_7001 = promo_7001 in promo_list_7001
promo_tidak_tersedia_7001 = promo_7001 not in promo_list_7001

# COMPARISON
belanja_min_7001 = total_7001 >= 200000
barang_min_7001 = jumlah_7001 >= 3

# LOGIC
diskon_7001 = member_7001 and belanja_min_7001
promo_valid_7001 = promo_tersedia_7001 and (barang_min_7001 or member_7001)
bukan_member_7001 = not member_7001

# ARITHMETIC
diskon_rp_7001 = total_7001 * 0.10 if diskon_7001 else 0
bayar_7001 = total_7001 - diskon_rp_7001
rata_7001 = total_7001 / jumlah_7001
sisa_7001 = total_7001 % jumlah_7001

# ASSIGNMENT
poin_7001 = 0
poin_7001 += jumlah_7001

# IDENTITY
kosong_7001 = None
cek_kosong_7001 = kosong_7001 is None
cek_bukan_7001 = kosong_7001 is not total_7001

# BITWISE
kode_7001 = 0
if member_7001:
    kode_7001 |= 1
if belanja_min_7001:
    kode_7001 |= 2
if barang_min_7001:
    kode_7001 |= 4
if promo_tersedia_7001:
    kode_7001 |= 8

cek_member_7001 = kode_7001 & 1
cek_belanja_7001 = kode_7001 & 2
xor_7001 = kode_7001 ^ 11
shift_7001 = kode_7001 << 1

# AKSES
akses_7001 = member_7001 and (belanja_min_7001 or promo_valid_7001)

print("\n=== DATA PELANGGAN ===")
print("Nama:", nama_7001)
print("Member:", member_7001)
print("Total:", total_7001)
print("Jumlah:", jumlah_7001)
print("Promo:", promo_7001)

print("\n=== HASIL PERHITUNGAN ===")
print("Diskon:", diskon_rp_7001)
print("Total Bayar:", bayar_7001)
print("Rata-rata:", rata_7001)
print("Sisa:", sisa_7001)
print("Poin:", poin_7001)

print("\n=== HASIL VALIDASI ===")
print("Belanja >= 200000:", belanja_min_7001)
print("Jumlah >= 3:", barang_min_7001)
print("Promo tersedia:", promo_tersedia_7001)
print("Promo tidak tersedia:", promo_tidak_tersedia_7001)
print("Promo valid:", promo_valid_7001)

print("\n=== IDENTITY & BITWISE ===")
print("None is None:", cek_kosong_7001)
print("is not:", cek_bukan_7001)
print("Kode bit:", format(kode_7001, "04b"))
print("Member &:", cek_member_7001)
print("Belanja &:", cek_belanja_7001)
print("XOR:", format(xor_7001, "04b"))
print("Shift <<:", format(shift_7001, "04b"))

print("\nHak akses:", akses_7001)
print("=== PROGRAM SELESAI ===")