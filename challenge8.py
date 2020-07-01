import os
from sys import exit

lineNum = 0

def detectDuplicates(line, chunkSize):
    
    global lineNum
    lineNum += 1
    length = len(line)
    if not length % chunkSize == 0:
        print("Invalid Chunk Size in:")
        print(line)
        print(f"Length: { len(line) } not a multiple of chunk size: { chunkSize }")
        exit(1)

    chunks = []
    for i in range(0, length, chunkSize):
        chunk = line[i:i+chunkSize]
        chunks.append(chunk)
    
    uniqueChunks = set(chunks)
    noOfUniques = len(uniqueChunks)
    total = len(chunks)
    if len(uniqueChunks) == len(chunks):
        return 0

    print(f"Found Duplicates in Line #{lineNum}")
    duplicateChunks = []
    for uniqueChunk in uniqueChunks:

        count = chunks.count(uniqueChunk)
        if count > 1:
            print(f"Duplicates: {count}")
            duplicateChunks.append(uniqueChunk)

    print("Duplicate Chunks:")
    print(duplicateChunks)
    print("="*60)
    startColor = "\033[93m"
    endColor = "\033[0m"
    
    for chunk in chunks:
        
        if chunk not in duplicateChunks:
            print(chunk, end='')
            continue

        print(startColor+chunk+endColor, end='')
    
    print()
        
    
def main():

    directory = 'files'
    filename = '8.txt'
    path = os.path.join(directory, filename)

    with open(path, 'r') as f:
        lines = f.readlines()
        
    noOfLines = len(lines)
    chunkSize = 2 * 16 # Since the lines are in hex, 16 bytes = 32 hex
    for i in range(noOfLines):
        lines[i] = lines[i].rstrip()
        line = lines[i]
        detectDuplicates(line, chunkSize)

        
if __name__ == "__main__":
    main()


