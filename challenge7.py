import os
from utils.aes_ecb import ecb
from base64 import b64decode

def main():

    directory = 'files'
    filename = '7.txt'
    path = os.path.join(directory, filename)

    with open(path, 'r') as f:
        lines = f.readlines()
        length = len(lines)
        for i in range(length):
            lines[i] = lines[i].rstrip()
        
    ciphertext = ''.join(lines)
    ciphertext = bytes(ciphertext, 'ascii')
    print("Ciphertext:")
    print(ciphertext)

    key = b'YELLOW SUBMARINE'
    print(f"Key: { key }")

    aes = ecb(key)

    ciphertext = b64decode(ciphertext)
    plaintext = aes.decrypt(ciphertext)
    print("Plaintext: ")
    print(plaintext)
    print(plaintext.decode('ascii'))

if __name__ == "__main__":
    main()

