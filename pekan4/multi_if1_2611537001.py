#buat program kondisional if
#ipk_7001
#program ini menggunakan fungsi input

umur_7001 = int(input("input umur anda:" ))
sim_7001 = input("apakah anda sudah punya sim C(y/t) :")[0]

if umur_7001 >= 17 and sim_7001 == 'y' :
    print("anda sudah dewasa dan boleh membawa motor")

if umur_7001 >= 17 and sim_7001!= 'y' :
    print("anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_7001 < 17 and sim_7001 == 'y' :
     print("anda belum cukup umur untuk membawa motor")

if umur_7001 < 17 and sim_7001 != 'y' :
     print("anda belum cukup umur untuk membawa motor")
print("program selesai")