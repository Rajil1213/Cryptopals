from sys import exit

class Analysis:

    text = ""
    
    def __init__(self, txt=""):
        self.text = txt

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
    
    def getChunks(self, chunkSize, stream=''):

        if stream == '':
            stream = self.text
        
        length = len(stream)
        chunks = []
        step = 2 * chunkSize
        for i in range(0, length, step):
            j = i + step
            if j > length:
                break
            chunk = stream[i:j]
            chunks.append(chunk)
        
        return chunks

    
    def tranposeChunks(self, chunks):

        noOfChunks = len(chunks)
        length = len(chunks[0])
        for chunk in chunks:
            if not len(chunk) == length:
                print("Not all chunks of the same length")
                print(f"Best guess length: { length }")
                exit(1)
        
        # print(f"Length of each chunk = { length }")
        # print(f"Total no. of chunks = { noOfChunks }")
        transposed = list()
        for i in range(0, length, 2):
            value = ""
            for chunk in chunks:
                value += chunk[i:i+2] # one byte at a time
            transposed.append(value)
        
        # print(f"Length of each transposed chunk = { len(transposed[0]) }")
        return transposed
    
    def avgHamDist(self, stream='', chunkSize=2):

        chunks = self.getChunks(chunkSize, stream)
        noOfChunks = len(chunks)
        avgDistance = 0
        for i in range(0, noOfChunks, 2):
            j = i + 1
            if j >= noOfChunks:
                break
            chunk1 = chunks[i]
            chunk2 = chunks[j]
            dist = self.byteHamDist(chunk1, chunk2)
            avgDistance += dist / (8 * chunkSize) # 1 chunkSize = 8 bits
        
        avgDistance /= noOfChunks
        
        return avgDistance
        

# For debugging Hamming Distance of Two Strings
if __name__ == "__main__":
    text1 = input("enter text1: ")
    text2 = input("enter text2: ")
    distance = Analysis().strHamDist(text1, text2)
    print(f"Distance: { distance }")