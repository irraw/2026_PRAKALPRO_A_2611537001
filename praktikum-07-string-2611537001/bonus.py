# Name : Shaira Kezia Pratiwi
# NIM : 2611537001
# question bonus

teks = input("Masukkan kalimat: ")

bersih = ""
for huruf in teks.lower():
    if huruf.isalnum():
        bersih = bersih + huruf

depan = 0
belakang = len(bersih) - 1
beda = 0

while depan < belakang:
    if bersih[depan] != bersih[belakang]:
        beda = beda + 1
    depan = depan + 1
    belakang = belakang - 1

if beda == 0:
    print("Palindrome")
else:
    print("not a Palindrome")