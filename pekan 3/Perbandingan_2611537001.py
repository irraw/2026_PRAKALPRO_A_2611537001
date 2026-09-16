#angka1_7001
#program ini menggunakan fungsi input()
#nilai yang dimasukan akan di konversi menjadi tipe data integer
#program operatoer perbandingan dalam python

angka1_7001 = int(input("input angka-1:"))
angka2_7001 = int(input("input angka-2: ")) 

# lebih besar dari
hasil = angka1_7001 > angka2_7001
print("\nOperasi Lebih Besar Dari")
print("angka1_7001 > angka2_7001:", hasil)

# lebih kecil dari
hasil = angka1_7001 < angka2_7001
print("\nOperasi Lebih Kecil Dari")
print("angka1_7001 < angka2_7001:", hasil)

# lebih besar dari atausama dengan
hasil = angka1_7001 >= angka2_7001
print("\nOperasi Lebih Besar Dari Sama Dengan")
print("angka1_7001 >= angka2_7001:", hasil)

# lebih kecil dari atau sama dengan
hasil = angka1_7001 <= angka2_7001
print("\nOperasi Lebih Kecil Dari Sama Dengan")
print("angka1_7001 <= angka2_7001:", hasil)   

# sama dengan
hasil = angka1_7001 == angka2_7001
print("\nOperasi Sama Dengan")
print("angka1_7001 == angka2_7001:", hasil)

# tidak sama dengan
hasil = angka1_7001 != angka2_7001
print("\nOperasi Tidak Sama Dengan")
print("angka1_7001 != angka2_7001:", hasil)

#tambahan: perbandingan berantai dalam python
hasil = 0 < angka1_7001 < 100
print("\nPerbandingan Berantai")
print("0 < angka1_7001 < 100:", hasil)

hasil = 0 < angka2_7001 < 100
print("0 < angka2_7001 < 100:", hasil)