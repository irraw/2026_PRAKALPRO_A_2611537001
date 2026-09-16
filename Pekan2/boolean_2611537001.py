#Nilai_7001
#deklarasi variabel dengan tipe data boolean
is_lulus = True
is_cumlaude = True

#menggunakan boolean
nilai = 85
batas_lulus = 75

# Menentukan nilai boolean dari kondisi
status_kelulusan = nilai >= batas_lulus #Hasilnya akan true

print ("=== Check kelulusan ===")
print("Nilai:", nilai)
print("Apakah lulus?", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat cumlaude!")