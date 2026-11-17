# Name : Shaira Kezia Pratiwi
# NIM : 2611537001
# question 6

full_name = "Shaira Kezia Pratiwi"
nim = "2611537001"

clean = full_name.strip() + " " + nim[:-3]
space = clean.find(" ")

if space == -1:
    first = clean
else:
    first = clean[:space]

full_name = first.lower() + nim[-3:]
print(full_name)