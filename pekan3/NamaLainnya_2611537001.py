#angka1_7001
#program ini menggunakan fungsi input()
#program operator keanggotaan dan identitas
print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

#input beberapa data yang dipisahkan dengan koma
input_data = input ("masukan beberapa angka, pisahkan dengan koma: ")

#mengubah input menjadi list integer 
data = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("memasukan angka yang ingin dicari: "))

#operator in
hasil_7001 = nilai_dicari in data
print("\nOperator keanggotaan IN")
print(nilai_dicari, "in", data, "=", hasil_7001)

#operator not in
hasil_7001 = nilai_dicari not in data
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari, "not in", data, "=", hasil_7001)

print("===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

# objek1 menggunakan list dari input 
objek1 = data

#objek2 merujuk pada objek yang sama dengan objek1
objek2 = objek1

#objek3 memiliki isi yang sama, tetaapi merupaan objek terbaru
objek3 = data.copy()

print("objek1 =", objek1)
print("objek2 =", objek2)
print("objek3 =", objek3)

#operator is
hasil_7001 = objek1 is objek2
print("\nOperator idetitas IS")
print("objek1 is objek2 =", hasil_7001)

#operator is not
hasil_7001 = objek1 is not objek3
print("\nOperator idetitas IS NOT")
print("objek1 is not objek3 =", hasil_7001)

#membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1 is objek3)
print("objek1 == objek3", objek1 == objek3)