import base64

key ='Code_in_Place_2021'

print('What encrypted messge do you want to send: ')
message = input()
encryptArray = []
for i in range(len(message)):
    key_c = key[i % len(key)]
    encryptArray.append(chr((ord(message[i]) + ord(key_c)) % 256))

encryption = base64.urlsafe_b64encode("".join(encryptArray).encode()).decode()
print("This is the encrypted message:\n" + encryption)

decryptArray = []
message = base64.urlsafe_b64decode(encryption).decode()
for i in range(len(message)):
    key_c = key[i % len(key)]
    decryptArray.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

print('This is the decryption of your message:\n' + "".join(decryptArray))