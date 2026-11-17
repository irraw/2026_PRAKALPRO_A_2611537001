# Name : Shaira Kezia Pratiwi
# NIM : 2611537001
# question 7

name = "Shaira Kezia Pratiwi"
nim = "2611537001"

username = name.split()[0] + nim[-3:]
intake = "20" + nim[:2]
lebar_kartu = 30
garis = "=" * lebar_kartu

print(garis)
print("STUDENT CARD".center(lebar_kartu))
print(garis)
print(f"{'Name':<10} : {name.title()}")
print(f"{'NIM':<10} : {nim}")
print(f"{'Username' :<10} : {username}")
print(f"{'intake' :<10} : {intake}")
print(garis)