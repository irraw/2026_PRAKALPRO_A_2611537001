#ulang_7001
#program ini menggunakan fungsi input()

ulang_7001 = int(input("masukan jumlah perulangan: "))
print("perulangan ke-0 sampat ke-", ulang_7001-1)
for i in range(ulang_7001):
    print(i, end= " ")
print()
print("perulangan ke-1 sampai ke-", ulang_7001)
for i in range(1,ulang_7001+1):
    print(i, end=" ")