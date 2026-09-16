#a1_7001
#program ini menggunakan fungsi input()
#program operator logika dalam python

#memasukan nilai boolean
#input tidak peka terhadap huruf besar dan kecil
a1_7001 = input("input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_7001 = input("input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1_7001:", a1_7001)
print("A2_7001:", a2_7001)

#konjungsi: bernilai True jika kedua operand bernilai True
hasil = a1_7001 and a2_7001
print("\nKonjungsi (AND)")
print("A1_7001 and A2_7001 =", hasil)

#disjungsi: bernilai True jika salah satunya true
hasil = a1_7001 or a2_7001
print("\nDisjungsi (OR)")
print("A1_7001 or A2_7001 =", hasil)

#negasi A1_7001: membalik nilai A1_7001
hasil = not a1_7001
print("\nNegasi A1_7001 (NOT)")
print("not A1_7001 =", hasil)

#negasi A2_7001: membalikan nilai A2_7001 
hasil = not a2_7001
print("\nNegasi A2_7001 (NOT)")
print("not A2_7001 =", hasil)

#XOR: bernilai true jika kedua bilangan berbeda
hasil = a1_7001 != a2_7001
print("\nDiskonjungsi ekslusif (XOR)")
print("A1_7001 XOR A2_7001 =", hasil)