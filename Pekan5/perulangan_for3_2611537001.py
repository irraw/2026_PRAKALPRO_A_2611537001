#ulang_7001
#program ini menggunakan fungsi input()

ulang_7001 = int(input("masukan jumlah perulangan: "))

jumlah_7001 = 0
for i in range(1, ulang_7001 + 1):
    print(i, end= " ")
    jumlah_7001 = jumlah_7001 +1

    if i < ulang_7001:
     print("+", end=" ") 
    else:
      print(" = ",jumlah_7001, end=" ")
print()
print("jumlah =", jumlah_7001)