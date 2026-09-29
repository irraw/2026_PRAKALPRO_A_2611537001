#ulang_7001
#program ini menggunakan fungsi input()

batas_7001 = int(input("masukan nilai batas: "))
for i in range (batas_7001 +1) :
    for j in range (batas_7001 +1) :
        print(i+j, end=" ")
    print() #pindah ke baris berikutnya
