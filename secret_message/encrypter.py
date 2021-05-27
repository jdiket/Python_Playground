import base64\

print('What encrypted messge do you want to send: ')
message = input()

print('Please enter an encryption key: ')
key = input()


encryptArray = []
for i in range(len(message)):
    key_c = key[i % len(key)]
    encryptArray.append(chr((ord(message[i]) + ord(key_c)) % 256))

encryption = base64.urlsafe_b64encode("".join(encryptArray).encode()).decode()
print("This is the encrypted message:\n" + encryption)