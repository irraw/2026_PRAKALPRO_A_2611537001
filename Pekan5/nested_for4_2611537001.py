# ulang_1234
# Program ini menggunakan fungsi input()

tinggi_7001 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_7001 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_7001 = tinggi_7001
    c_7001 = a_7001
    lebar_7001 = (2 * tinggi_7001) - 2

    for i in range(1, tinggi_7001 + 1):
        b_7001 = c_7001 + 1

        for j in range(1, lebar_7001 + 1):

            # Baris atas dan bawah
            if i == 1 or i == tinggi_7001:
                if j == 1 or j == lebar_7001:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j == 1 or j == lebar_7001:
                    print("|", end="")
                else:
                    if j == c_7001:
                        print("<", end="")
                    elif j == b_7001:
                        print(">", end="")
                    elif j == (lebar_7001 - c_7001):
                        print("<", end="")
                    elif j == (lebar_7001 - c_7001 + 1):
                        print(">", end="")
                    elif j > b_7001 and j < (lebar_7001 - c_7001):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_7001 -= 2

        if a_7001 <= 0:
            c_7001 = (-a_7001) + 2
        else:
            c_7001 = a_7001