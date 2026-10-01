print("=== PROGRAM JAM PASIR KRISTAL ===")
n_7001 = int(input("Masukkan ukuran skala jam pasir: "))

print("#", end="")
for b_7001 in range(4 * n_7001 + 5):
    print("=", end="")
print("#")

for baris_7001 in range(n_7001, 0, -1):
    print("| ", end="")
    for s_7001 in range(2 * (n_7001 - baris_7001)):
        print(" ", end="")
    for angka_7001 in range(baris_7001, 0, -1):
        print(angka_7001, end=" ")
    print("<*>", end="")
    for angka_7001 in range(1, baris_7001 + 1):
        print("", angka_7001, end="")
    # spasi penyeimbang kanan
    for s_7001 in range(2 * (n_7001 - baris_7001)):
        print(" ", end="")
    print(" |", end="")
    print()

print("|", end="")
for s_7001 in range(2 * n_7001 + 1):
    print(" ", end="")
print("<*>", end="")
for s_7001 in range(2 * n_7001 + 1):
    print(" ", end="")
print("|", end="")
print()

for baris_7001 in range(1, n_7001 + 1):
    print("| ", end="")
    for s_7001 in range(2 * (n_7001 - baris_7001)):
        print(" ", end="")
    for angka_7001 in range(baris_7001, 0, -1):
        print(angka_7001, end=" ")
    print("<*>", end="")
    for angka_7001 in range(1, baris_7001 + 1):
        print("", angka_7001, end="")
    for s_7001 in range(2 * (n_7001 - baris_7001)):
        print(" ", end="")
    print(" |", end="")
    print()

print("#", end="")
for b_7001 in range(4 * n_7001 + 5):
    print("=", end="")
print("#")