from utils.BinaryMap import BinaryMap
from utils.BinaryOps import BinaryOps

def main():

    arg1 = input("First Argument: ")
    arg2 = input("Second Argument: ")
    
    arg1 = BinaryMap.hexToBinary(arg1)
    arg2 = BinaryMap.hexToBinary(arg2)

    result = BinaryOps.xor(arg1, arg2)
    result = BinaryMap.binaryToHex(result)

    print(f"XOR result = { result }")

main()