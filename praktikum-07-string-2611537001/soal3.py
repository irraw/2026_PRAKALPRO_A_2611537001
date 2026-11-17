# Name : Shaira Kezia Pratiwi
# NIM : 2611537001
# question 3

text = "Informatika"
print(text[10])
print(text.upper ())
print(text[0:20])

#B
text = "Shaira Kezia Pratiwi"
count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)