""" Challenge 1: Perform Base64 encoding of Hex String """

from sys import argv, exit
from utils.BinaryMap import BinaryMap

def main():
    if not len(argv) == 2:
        print("Usage python3 challenge1.py <hex value>")
        exit(1)
    decimal = int(argv[1], base=16)
    binary = bin(decimal)[2:]
    base64Val = BinaryMap.binaryToBase64(binary)
    print(f"Base64 Equivalent: { base64Val }")
        
main()
