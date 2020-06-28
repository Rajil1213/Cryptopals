class Analysis:

    def toBytes(self, text):

        textBytes = ""
        for letter in text:
            asciiVal = ord(letter)
            hexVal = hex(asciiVal)
            hexVal = hexVal[2:]
            if len(hexVal) == 1:
                hexVal = '0' + hexVal
            textBytes += hexVal
        
        return textBytes
    
    def strHamDist(self, text1, text2):
        
        text1Bytes = self.toBytes(text1)
        text2Bytes = self.toBytes(text2)

        return self.byteHamDist(text1Bytes, text2Bytes)
    
    def byteHamDist(self, bytes1, bytes2):

        decimal1 = int(bytes1, base=16)
        decimal2 = int(bytes2, base=16)

        result = bin(decimal1 ^ decimal2)[2:]
        distance = result.count('1')

        return distance


if __name__ == "__main__":
    text1 = input("enter text1: ")
    text2 = input("enter text2: ")
    distance = Analysis().strHamDist(text1, text2)
    print(f"In Bytes: { distance }")