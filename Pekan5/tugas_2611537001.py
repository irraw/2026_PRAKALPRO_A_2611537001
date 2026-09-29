#tugas_7001

tinggi_7001 = int(input("masukan tinggi pola: "))

# baris spasi
for i_7001 in range (1, tinggi_7001 + 1) :
    for j_7001 in range(tinggi_7001 - i_7001) :
        print(" ", end="")

# baris titik
    for a in range(i_7001) :
        print("* ", end="")
    print()