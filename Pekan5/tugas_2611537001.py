#tugas_7001

tinggi_7001 = int(input("masukan tinggi pola: "))

# baris spasi
for i in range (1, tinggi_7001 + 1) :
    for j in range(tinggi_7001 - i) :
        print(" ", end="")

# baris titik
    for a in range(i) :
        print("* ", end="")
    print()