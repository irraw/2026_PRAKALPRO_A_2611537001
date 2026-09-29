#ulang_7001
#program ini menggunakan fungsi input()

batas_7001 = int(input("masukan nilai batas: "))
for line in range (1, batas_7001 + 1) :
    for j in range(1, (-1 * line + batas_7001) + 1):
        print (".", end=" ")
    print(line)