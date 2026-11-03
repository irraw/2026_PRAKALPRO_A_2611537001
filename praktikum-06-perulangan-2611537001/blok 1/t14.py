attempt = 1
correct_pin = "1234"
MAX_ATTEMPTS = 3
pin = input("Enter your PIN:")
while pin != correct_pin and attempt <= MAX_ATTEMPTS:
    attempt += 1
if pin == correct_pin:
    print("Access granted")
else:
    print("Incorrect PIN")
    print("Account locked")
    