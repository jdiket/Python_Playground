import base64\

print('What encrypted messge do you want to send: ')
message = input()

print('Please enter an encryption key: ')
key = input()


enc = []
for i in range(len(message)):
    key_c = key[i % len(key)]
    enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

encryption = base64.urlsafe_b64encode("".join(enc).encode()).decode()
print("This is the encrypted message:\n" + encryption)