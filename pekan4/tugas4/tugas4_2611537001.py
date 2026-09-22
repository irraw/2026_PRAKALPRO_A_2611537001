print("=== DATA PENGUNJUNG TAMAN BERMAIN ===")

#INPUT
nama_pengunjung_7001 = (input("masukan nama pengunjung: "))
umur_7001 = int(input("masukan umur pengunjung: "))
sim_7001 = input("apakah anda sudah punya sim C(y/t) :")[0]

print("\nPemilihan paket wahana (1-5): ")
print("1. Safari Rimba         (Rp 50,000)")
print("2. Arung Jeram          (Rp 75,000)")
print("3. Motor ATV Ekstrim    (Rp 120,000)")
print("4. Roller Coaster Kilat (Rp 100,000)")
print("5. All-Access VIP       (Rp 220,000)")

nomor_paket_7001 = int(input("masukan nomor paket (1-5): "))
jumlah_tiket_7001 = int(input("masukan jumlah tiket: "))
member_7001 = input("apakah kamu member (y/t): "). lower()
kode_promo_7001 = input("apakah kode promo valid (y/t): "). lower()

match nomor_paket_7001:
    case 1:
        nama_paket_7001 = "Safari Rimba"
        harga_satuan_7001 = 50000
    case 2:
        nama_paket_7001 = "Arung Jeram"
        harga_satuan_7001 = 75000
    case 3:
        nama_paket_7001 = "Motor ATV Ekstrim"
        harga_satuan_7001 = 120000
    case 4:
        nama_paket_7001 = "Roller Coaster Kilat"
        harga_satuan_7001 = 100000
    case 5:
        nama_paket_7001 = "All-Access VIP"
        harga_satuan_7001 = 220000
    case _:
        nama_paket_7001 = "Tidak Valid"
        harga_satuan_7001 = 0

print("\n--- KELAYAKAN PENGGUNAAN WAHANA---")

if nomor_paket_7001 == 3:
    if umur_7001 >= 17 and sim_7001 == 'y' :
     print("Anda sudah dewasa dan boleh mengendarai ATV sendiri.")
    elif umur_7001 >= 17 and sim_7001!= 'y' :
     print("Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)")
    elif umur_7001 < 17 and sim_7001 == 'y' :
     print("Identitas tidak valid: Belum cukup umur memiliki SIM")    
    else:
       print("Anda belum cukup umur dan tidak boleh bawa motor ATV")
else: 
   if nomor_paket_7001 != 3:
    if umur_7001 <= 5:
     print("status akses: pengunjung balita, wajib di damping1 orang dewasa di {nama_paket_7001}.")
    elif umur_7001 >= 60:
     print("status akses: pengunjung senior, mendapat jalur khusus di {nama_paket_7001}")
    else:
      print("status akses: silahkan menikmati wahana {nama_paket_7001}")

subtotal_7001 = harga_satuan_7001 * jumlah_tiket_7001
persen_diskon_7001 = 0

if subtotal_7001 >= 200000 :
   persen_diskon_7001 += 10 #diskon belanja besar
if member_7001 == "y" or member_7001 == "ya" :
   persen_diskon_7001 += 5 #diskon member
if kode_promo_7001 == "y" or kode_promo_7001 == "ya" :
   persen_diskon_7001 += 15 #diskon voucher promo
if jumlah_tiket_7001 >= 5 :
   persen_diskon_7001 += 5 #diskon tambahan rombongan

total_diskon_7001 = int(subtotal_7001 * (persen_diskon_7001 / 100))
total_bayar_7001 = subtotal_7001 - total_diskon_7001

print("\n--- Rincian Pembayaran ---")
print(f"subtotal Belanja : Rp {subtotal_7001:,}")
if subtotal_7001 > 300000: 
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
print(f"Total Diskon     : {persen_diskon_7001}% (Rp {int(total_diskon_7001):,})")
print(f"Total Bayar      : Rp {int(total_bayar_7001):,}")
print("Catatan Layanan  : Terima kasih telah berkunjung.")
print("Program Selesai") 