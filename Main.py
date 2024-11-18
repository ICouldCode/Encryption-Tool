from cryptography.fernet import Fernet
import os
import itertools
import sys
import time
import threading

cmd = input("Generate key? [1]yes [2]no\n")
key = Fernet.generate_key()

if(cmd == "1"):
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    

with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

fernet = Fernet(key)

cmd = input("[1]encrpyt [2]decrpyt\n")

while True:
    filePath = input("Input file path: ")
    if os.path.exists(filePath):
        break
    print("Invalid path, try again\n")

if(cmd == "1"):
    with open(filePath, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)

    with open(filePath, 'wb') as encryptedFile:
        encryptedFile.write(encrypted)
else:
    with open(filePath, 'rb') as encFile:
        encrypted = encFile.read()

    decrypted = fernet.decrypt(encrypted)

    with open(filePath, 'wb') as decFile:
        decFile.write(decrypted)

done = False

def animation():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rloading ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\Complete!     ')

t = threading.Thread(target=animation)
t.start()

#long process here
time.sleep(2)
done = True
