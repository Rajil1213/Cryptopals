from utils.XOR import AsciiXOR

def main():

    # Example of Encryption According to the Challenge Specification
    key = "ICE"
    plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print("Example:")
    print(f"Plaintext: { plaintext }")
    print(f"Key: { key }")
    while True:
        
        encode = AsciiXOR(plaintext)

        result = encode.repeatKeyEncrypt(key)
        print(f"Ciphertext: { result }")
        
        again = input("Enter 'y' To Encrypt Another: ")
        if not again.lower() == 'y':
            break
        
        plaintext = input("Enter Text to Encrypt: ")
        key = input("Enter Key: ")

if __name__ == "__main__":
    main()
