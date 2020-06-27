from sys import argv, exit
from utils.BinaryMap import BinaryMap

def main():

    if not len(argv) == 2:
        print("Usage: python3 BinaryMap.py <hex string>")
        exit(1)

    hexValue = argv[1]
    mapping = BinaryMap()
    # convert hex to binary
    binaryValue = mapping.hexToBinary(hexValue)
    # convert binary to base64
    base64Value = mapping.binaryToBase64(binaryValue)

    print(f"Base64 Equivalent: { base64Value }")

main()