#buat program untuk kondisional if
#ipk_7001
#program ini menggunakan fungsi input

umur_7001 = int(input("input umur anda:" ))
sim_7001 = input("apakah anda sudah punya sim C(y/t) :")[0]

if umur_7001 >= 17 and sim_7001 == 'y' :
    print("anda sudah dewasa dan boleh membawa motor")
elif umur_7001 >= 17 and sim_7001!= 'y' :
    print("anda sudah dewasa tetapi tidak boleh bawa motor")
elif umur_7001 < 17 and sim_7001 == 'y' :
     print("anda belum cukup umur untuk punya sim")
else :
     print("anda belum cukup umur dan tidak boleh membawa motor")
print("program selesai")
