from math import inf
import os
from utils.toolkit import Toolkit
from utils.XOR import AsciiXOR
from utils.BinaryMap import BinaryMap

def getKeyLength(hexVal):

    actualKeyLength = 2
    minDistance = inf
    analyse = Toolkit(hexVal)
    for keyLength in range(2, 41):
        distance = analyse.avgHamDist(chunkSize=keyLength)
        # print(f"KeyLength: { keyLength }, Hamming Distance: { distance }")
        if distance < minDistance:
            minDistance = distance
            actualKeyLength = keyLength 
    
    return actualKeyLength
    
def getKeys(tranposedChunks):

    pearsonKey = ""
    chiSquareKey = ""
    commonKey = ""
    for chunk in transposedChunks:

        decrypt = AsciiXOR(chunk)
        pearsonResult = decrypt.pearsonRank(1, get=True)
        chiSquareResult = decrypt.chisquareRank(1, get=True)
        commonResult = decrypt.commonRank(1, get=True)
        
        pearsonKey += chr(pearsonResult[2])
        chiSquareKey += chr(chiSquareResult[2])
        commonKey += chr(commonResult[2])

    """ Debug
    print(f"By Karl Pearson Metric, Key: { pearsonKey }")
    print(f"By Chi-squared Metric, Key: { chiSquareKey }")
    print(f"By Common Metric, Key: { commonKey }")
    """
    return pearsonKey, chiSquareKey, commonKey

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

    analyse = Toolkit(hexVal)
    chunks = analyse.getChunks(chunkSize=actualKeyLength)
    transposedChunks = analyse.tranposeChunks(chunks)
    """ Debug
    print(f"No. of chunks = { len(chunks) }")
    print(f"No. of transposed chunks = { len(transposedChunks) }")
    print(f"Length of a tranposed chunk = { len(transposedChunks[0]) }")
    """
    # keys = getKeys(tranposedChunks)
    commonKey = "Terminator X: Bring the noise" # keys[2]
    pearsonKey = "Terminator X: Bring the noIse" # keys[0]
    chiSquareKey = "Terminator X: Bring the ioise" # keys[1]
    decrypt = AsciiXOR(hexVal)
    decryptCommon = decrypt.repeatKeyDecrypt(commonKey)
    decryptPearson = decrypt.repeatKeyDecrypt(pearsonKey)
    decryptChiSquare = decrypt.repeatKeyDecrypt(chiSquareKey)
    print("From Common: ")
    print(decryptCommon)
    print("From Pearson: ")
    print(decryptPearson)
    print("From ChiSquare: ")
    print(decryptChiSquare)
        

if __name__ == "__main__":
    main()
