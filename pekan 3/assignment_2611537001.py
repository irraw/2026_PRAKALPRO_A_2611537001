#angka1_7001
#program ini menggunakan fungsi input()
#nilai yang dimasukan akan di konversi menjadi tipe data interger
#program operator assignment dalam python

angka1_7001 =int(input("input angka-1:"))
angka2_7001 =int(input("input angka-2:"))

print("\nNilai awal angka1_7001 =", angka1_7001)
print("nilai angka2 =", angka2_7001)

#assignment biasa
hasil_7001 = angka1_7001
print("\nAssignment biasa (=")
print("hasil_7001 =", hasil_7001)

#assignment penambahan
hasil_7001 = angka1_7001
hasil_7001 += angka2_7001
print("\nAssignment menambahan (+=)")
print("hasil_7001 =", hasil_7001)

#assignment pengurangan 
hasil_7001 = angka1_7001
hasil_7001 -= angka2_7001
print("\nAssigment penambahan (-=)")
print("hasil_7001 =", hasil_7001)

#assignment perkalian
hasil_7001= angka1_7001
hasil_7001 *= angka2_7001
print("\nAssigment perkalian (*=)")
print("hasil_7001 =", hasil_7001)

#assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_7001 != 0:
    hasil_7001 = angka1_7001
    hasil_7001 /= angka2_7001
    print("\nAssigment pembagian (/=)")
    print("hasil_7001 =", hasil_7001)
    #operator tambahan  
    hasil_7001 = angka1_7001
    hasil_7001 //= angka2_7001
    print("\nAssigment pembagian bulat (//=)")
    print("hasil_7001 =", hasil_7001)
    hasil_7001 = angka1_7001
    hasil_7001 %= angka2_7001
    print("\nAssigment sisa bagi (%=)")
    print("hasil_7001 =", hasil_7001)
else:
    print("\nPembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh bernilai 0")

#operator tambahan: assignment perpangkatan
hasil_7001 = angka1_7001
hasil_7001 **= angka2_7001
print("\nAssigment berpangkatan (**=)")
print("hasil_7001 =", hasil_7001)
