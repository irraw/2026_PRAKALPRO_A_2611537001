#buat program untuk match case
#ipk_7001
#program ini menggunakan fungsi input()
#program konversi angka menjadi nama bulan

bulan_7001 = int(input("masukan angka bulan (1-12):"))

match bulan_7001:
    case 1:
        print("januari")
    case 2:
        print("februari")
    case 3:
            print("maret")
    case 4:
            print("april")
    case 5:
            print("mei")
    case 6:
            print("juni")
    case 7:
            print("juli")
    case 8:
            print("agustus")
    case 9:
            print("september")
    case 10:
            print("oktober")
    case 11:
            print("november")
    case 12:
            print("desember")
    case _:
            print("angka tidak valid")