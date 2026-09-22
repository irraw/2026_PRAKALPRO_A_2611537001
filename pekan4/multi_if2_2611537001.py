#buat program untuk kondisional if
#total_belanja_7001
#program ini menggunakan fungsi input
#program menghitung diskon belanja

#input dari user
total_belanja_7001 = float(input("masukan total belanja (Rp) : "))

#input status member (mengecek apakag user mengetik 'y' atau 'ya') 
input_member_7001 = input("apakah anda member? (y/t) : ").strip( ).lower( )
is_member_7001 = input_member_7001 in ["y","ya"]

#input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_7001 = input("apakah kode promo valid? (y/t):").strip( ).lower( )
kode_promo_valid_7001 = input_promo_7001 in ["y","ya"]

total_diskon_persen_7001 = 0

#multi-if terpisah: setiap kondisi diperiksa secara independen
#diskon bisa di tumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_7001 > 1000000:
    total_diskon_persen_7001 += 10 # diskon belanja besar

if is_member_7001:
    total_diskon_persen_7001 += 5 # diskon member

if kode_promo_valid_7001:
    total_diskon_persen_7001 += 15 #diskon voucher

#menghitung nominal diskon dan total bayar
nominal_diskon_7001 = total_belanja_7001 * (total_diskon_persen_7001 / 100)
total_bayar_7001 = total_belanja_7001 - nominal_diskon_7001

#output hasil 
print("\n--- Rincian pembayaran ---")
print(f"total diskon : {total_diskon_persen_7001}% (Rp{nominal_diskon_7001:,.0f})")
print(f"total bayar  : Rp {total_bayar_7001:,.0f}")

print(f"total diskon yang anda dapatkan : {total_diskon_persen_7001}%")
#output: total diskon yang anda dapatkan: 30% jika belanja > 1 juta,member, dan kode promo valid