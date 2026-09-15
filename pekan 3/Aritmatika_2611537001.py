#angka1_7001
#program ini menggunakan fungsi input ()
#nilai yang dimasukan akan di konversi menjadi tipe data integer

angka1 = int(input("input angka-1:"))
angka2 = int(input("input angka-2: "))

#penjumlahan
hasil = angka1 + angka2
print("\nOperasi Penjumlahan")
print("hasil =", hasil)

#pengurangan
hasil = angka1 - angka2
print("\nOperasi Pengurangan")
print("hasil =", hasil)

#Perkalian
hasil = angka1 * angka2
print("\nOperasi Perkalian")        
print("hasil =", hasil)

#pembagian, pembagian bulat, dan sisa bagi
if angka2 != 0:
    hasil = angka1 / angka2
    print("\nOperasi Pembagian")
    print("hasil =", hasil)

    hasil = angka1 // angka2
    print("\nOperasi Pembagian Bulat")
    print("hasil =", hasil)

    hasil = angka1 % angka2
    print("\nOperasi Sisa Bagi")
    print("hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0.")

    #pangkat
hasil = angka1 ** angka2
print("\nOperasi Pangkat")
print("hasil =", hasil)