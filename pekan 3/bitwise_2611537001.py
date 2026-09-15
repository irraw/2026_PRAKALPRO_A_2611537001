#angka1_7001
# Program ini menggunakan fungsi input()

print("========================================")
print("3. OPERATOR BITWISE")
print("========================================")

angka1_7001 = int(input("Masukkan angka bitwise-1: "))
angka2_7001 = int(input("Masukkan angka bitwise-2: "))

print("Angka dalam bentuk desimal dan biner")
print("angka1 =", angka1_7001, "| biner =", bin(angka1_7001))
print("angka2 =", angka2_7001, "| biner =", bin(angka2_7001))

# Bitwise AND
hasil_7001 = angka1_7001 & angka2_7001
print("\nBitwise AND (&)")
print(angka1_7001, "&", angka2_7001, "=", hasil_7001)
print("Biner hasil =", bin(hasil_7001))
print("Biner hasil (8 bit) =", format(hasil_7001, "08b"))

# Bitwise OR
hasil_7001 = angka1_7001 | angka2_7001
print("\nBitwise OR (|)")
print(angka1_7001, "|", angka2_7001, "=", hasil_7001)
print("Biner hasil =", bin(hasil_7001))
print("Biner hasil (8 bit) =", format(hasil_7001, "08b"))

# Bitwise XOR
hasil_1017 = angka1_7001 ^ angka2_7001
print("\nBitwise XOR (^)")
print(angka1_7001, "^", angka2_7001, "=", hasil_7001)
print("Biner hasil =", bin(hasil_7001))
print("Biner hasil (8 bit) =", format(hasil_7001, "08b"))

# Bitwise NOT
hasil_1017 = ~angka1_7001
print("\nBitwise NOT (~)")
print("~", angka1_7001, "=", hasil_7001)
print("Biner hasil =", bin(hasil_7001))
print("Biner hasil (8 bit) =", format(hasil_7001, "08b"))

# Bitwise geser kiri
jumlah_geser_7001 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_7001 = angka1_7001 << jumlah_geser_7001
print("\nBitwise geser kiri (<<)")
print(angka1_7001, "<<", jumlah_geser_7001, "=", hasil_7001)
print("Biner hasil =", bin(hasil_7001))
print("Biner hasil (8 bit) =", format(hasil_7001, "08b"))

# Bitwise geser kanan
hasil_7001 = angka1_7001 >> jumlah_geser_7001
print("\nBitwise geser kanan (>>)")
print(angka1_7001, ">>", jumlah_geser_7001, "=", hasil_7001)
print("Biner hasil =", bin(hasil_7001))
print("Biner hasil (8 bit) =", format(hasil_1017, "08b"))