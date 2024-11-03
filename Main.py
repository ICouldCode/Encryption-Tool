from cryptography.fernet import Fernet

cmd = input("Generate key? [1]yes [2]no\n")
key = Fernet.generate_key()

if(cmd == "1"):
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    

with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

fernet = Fernet(key)

cmd = input("[1]encrpyt [2]decrpyt\n")

if(cmd == "1"):
    with open('test.txt', 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)

    with open('test.txt', 'wb') as encryptedFile:
        encryptedFile.write(encrypted)
else:
    with open('test.txt', 'rb') as encFile:
        encrypted = encFile.read()

    decrypted = fernet.decrypt(encrypted)

    with open('test.txt', 'wb') as decFile:
        decFile.write(decrypted)