from math import inf
import os
from utils.toolkit import Analysis
from utils.BinaryMap import BinaryMap

def getKeyLength(hexVal):

    actualKeyLength = 2
    minDistance = inf
    analyse = Analysis(hexVal)
    for keyLength in range(2, 41):
        distance = analyse.avgHamDist(chunkSize=keyLength)
        # print(f"KeyLength: { keyLength }, Hamming Distance: { distance }")
        if distance < minDistance:
            minDistance = distance
            actualKeyLength = keyLength 
    
    return actualKeyLength
    

def main():

    directory = "files"
    filename = "6.txt"
    path = os.path.join(directory, filename)
    with open(path, 'r') as f:
        # read only 10 lines
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

    jumbo_base64 = ''.join(lines)
    binary = BinaryMap.base64ToBinary(jumbo_base64)
    decimal = int(binary, base=2)
    hexVal = hex(decimal)[2:]

    actualKeyLength = 29 # getKeyLength(hexVal) 
    # print(f"Key Length = { actualKeyLength }")

    analyse = Analysis(hexVal)
    chunks = analyse.getChunks(chunkSize=actualKeyLength)
    transposedChunks = analyse.tranposeChunks(chunks)

    

if __name__ == "__main__":
    main()
