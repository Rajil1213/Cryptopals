from aes import aes
from sys import exit

class ecb:

    key = b''
    BYTE = 16
    AES = "aes object to be initialized later"

    def __init__(self, key):
        if (len(key)) != self.BYTE:
            print("Key Length Error: Must be 16 Bytes Long")
            exit(1)
        self.key = key
        self.AES = aes(key)

    def encrypt(self, plaintext):

        length = len(plaintext)
        if length % self.BYTE != 0:
            padding = self.BYTE - (length % self.BYTE)
            padValue = hex(padding)[2:]
            padValue = bytes.fromhex(padValue)
            if len(padValue) == 1:
                padValue = '0' + padValue

            plaintext += padValue * padding
            length = len(plaintext)
        
        ciphertext = b""
        for i in range(0, length, self.BYTE):

            block = plaintext[i:i+self.BYTE]
            ciphered = self.AES.encrypt(block)
            ciphertext += ciphered
        
        return ciphertext
    
    def decrypt(self, ciphertext):

        # consider no padding, as not specified in the challenge
        length = len(ciphertext)
        if length % self.BYTE != 0:
            print("Ciphertext Length Error")
            exit(1)
        
        plaintext = b""
        for i in range(0, length, self.BYTE):

            block = ciphertext[i:i+self.BYTE]
            deciphered = self.AES.decrypt(block)
            plaintext += deciphered
        
        return plaintext


if __name__ == "__main__":

    plaintext = b"Two One Nine TwoTwo One Nine Two"
    key = b"Thats my Kung Fu"

    cipher = ecb(key) 
    ciphertext = cipher.encrypt(plaintext)
    print(ciphertext)
    
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)
    
