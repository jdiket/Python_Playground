import base64

print('Please enter the encoded message: ')
encryption = input()

print('Please enter the decryption key: ')
key = input()

dec = []
message = base64.urlsafe_b64decode(encryption).decode()
for i in range(len(message)):
    key_c = key[i % len(key)]
    dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

print('This is the decryption of your message:\n' + "".join(dec))