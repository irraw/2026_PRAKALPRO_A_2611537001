# Name : Shaira Kezia Pratiwi
# NIM : 2611537001
# question 5


#A
username = input("Username: ")

if len(username) < 5:
    print("invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha():
    print("must start with a letter")
else :
    print("Valid")

#B

NIM = input("Nim: ")

if len(NIM) == 10 and NIM.isdigit():
    print("Valid, intake year 20" + NIM[:2])
else:
    print("Invalid NIM")
    