from math import log2
from sys import argv, exit


class BinaryMap:

    @classmethod
    def getBinary(cls, n=6):

        twoBit = {"00", "01", "10", "11"}
        sixBit = ""
        sixBitBinary = []

        for firstCrumb in twoBit:
            for secondCrumb in twoBit:
                for thirdCrumb in twoBit:
                    sixBit = firstCrumb + secondCrumb + thirdCrumb
                    sixBitBinary.append(sixBit)

        if n == 6:
            return sixBitBinary
        
        start = 6 - n
        nBits = sixBitBinary[:2**n]
        nBitBinary = [value[start:] for value in nBits]

        return nBitBinary
        
    @classmethod
    def getBinaryMapping(cls, charset):

        n = len(charset)

        if not n % 2 == 0:
            print("No. of chars in charset must be even")
            exit(1)

        noOfBits = int(log2(n))
        binaryBits = cls.getBinary(noOfBits)

        mapping = dict()
        for i in range(n):
            key = charset[i]
            binaryVal = binaryBits[i]
            mapping[key] = binaryVal
        
        return mapping
    
    @classmethod
    def hexToBinary(cls, hex):
        
        hexCharset = "0123456789abcdef"
        hex2binary = cls.getBinaryMapping(hexCharset)
        binaryEquivalent = ""

        for char in hex:
            binaryEquivalent += hex2binary[char]

        return binaryEquivalent
    
    @classmethod
    def binaryToBase64(cls, binary):

        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        specials = "+/"
        base64Charset = uppercase + lowercase + numbers + specials 
        binary2base64 = cls.getBinaryMapping(base64Charset)
        binary2base64 = { value: key for (key, value) in binary2base64.items()}        
        base64Equivalent = ""

        padding = 0
        if len(binary) % 6 != 0:
            padding = 6 - (len(binary) % 6)
        
        zeros = '0' * padding
        equals = '=' * (padding // 2)

        binary += zeros
        n = len(binary)

        for i in range(0, n, 6):
            binaryVal = binary[i:i + 6]
            base64Equivalent += binary2base64[binaryVal]
            
        base64Equivalent += equals
        
        return base64Equivalent

if __name__ == "__main__":

    if not len(argv) == 2:
        print("Usage: python3 BinaryMap.py <hex string>")
        exit(1)

    hexValue = argv[1]
    mapping = BinaryMap()
    binaryValue = mapping.hexToBinary(hexValue)
    base64Value = mapping.binaryToBase64(binaryValue)

    print(f"Base64 Equivalent: { base64Value }")
