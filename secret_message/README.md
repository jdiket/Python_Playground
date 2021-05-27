# Secret Message App

This secret messaging service is broken into 3 files, one as a showcase and the other two for functionality.  The purpose is to encrypt a simple message between friends, peers, colleages, or really anyone and allow a fun way to keep it secret and away from prying eyes.  It was originally built for Stanford University's Code in Place 2021 Final Project

### secret_message.py

This is the demonstration of intent, not truly intended for functional use.  When this file runs it prompts the user for a message to encrypt, then runs through an encryption using Pythons Base64 module and provided key.  It then outputs the newly encrypted message, and runs through a decryption process and outputs, hopefully, the original message in plaintext.

### encrypter.py

When run, this program prompts the user for a message they want to encrypt, then a key with which to encrypt it.  It then goes through the encryption process using Base64 and outputs the encrypted message to send to a recipient.

### decrypter.py

The other side of the two part functionality.  This program prompts the user for the encrypted message and the encryption key that was used, then runs decryption and outputs the plain text message.