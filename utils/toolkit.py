from sys import exit

class Toolkit:

    text = ""
    
    def __init__(self, txt=""):
        """constructor for Toolkit

        Args:
            txt (str, optional): The Hex-valued String to apply toolkit on. Defaults to "".
        """
        self.text = txt

    def toBytes(self, text):
        """converts an ASCII string to a string of bytes in hex

        Args:
            text (str): an ASCII string

        Returns:
            str: string of bytes corresponding to `text`, in Hex
        """

        textBytes = ""
        for letter in text:
            asciiVal = ord(letter)
            hexVal = hex(asciiVal)
            # remove the '0x' prefix
            hexVal = hexVal[2:] 
            # convert 1 to 01, a to 0a and so on
            if len(hexVal) == 1:
                hexVal = '0' + hexVal 
            textBytes += hexVal
        
        return textBytes
    
    def strHamDist(self, text1, text2):
        """computers the bit-wise Hamming Distance between two strings

        Args:
            text1 (str): first string (ASCII)
            text2 (str): second string (ASCII)

        Returns:
            int: the Hamming distance between `text1` and `text2`
        """
        
        text1Bytes = self.toBytes(text1)
        text2Bytes = self.toBytes(text2)

        return self.byteHamDist(text1Bytes, text2Bytes)
    
    def byteHamDist(self, bytes1, bytes2):
        """computes the bit-wise Hamming Distance between two byte-streams

        Args:
            bytes1 (str): string representing the first byte-stream (in Hex)
            bytes2 (str): string representing the second byte-stream (in Hex)

        Returns:
            int: the Hamming Distance between `bytes1` and `bytes2`
        """

        decimal1 = int(bytes1, base=16)
        decimal2 = int(bytes2, base=16)

        result = bin(decimal1 ^ decimal2)[2:]
        distance = result.count('1')

        return distance
    
    def getChunks(self, chunkSize, stream=''):
        """converts `stream` into a list of smaller strings, each of size `chunkSize` bytes

        Args:
            chunkSize (int): size of each chunk, length of each string in the returned list
            stream (str, optional): String that is to be sliced into a list. Defaults to ''.

        Returns:
            list: list of substrings of `stream` each of size `chunkSize`, taken in order
        """

        if stream == '':
            stream = self.text
        
        length = len(stream)
        chunks = []
        # 1 chunkSize(byte) = 2 Hex values
        step = 2 * chunkSize
        for i in range(0, length, step):
            j = i + step
            # if list index out of range, exit
            if j > length:
                break
            chunk = stream[i:j]
            chunks.append(chunk)
        
        return chunks

    
    def tranposeChunks(self, chunks):
        """transposes chunks in `chunks`,
        e.g., 10 strings of 7 bytes each, get converted into 7 strings of 10 bytes each

        Args:
            chunks (list): list of strings to tranpose

        Returns:
            list: tranposed list of `chunks`
        """

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
        # length is in nibbles, we operate in bytes, so take step size as 2
        for i in range(0, length, 2):
            value = ""
            for chunk in chunks:
                # one byte at a time, one byte = 2 Hex values
                value += chunk[i:i+2]
            transposed.append(value)
        
        # print(f"Length of each transposed chunk = { len(transposed[0]) }")
        return transposed
    
    def avgHamDist(self, stream='', chunkSize=2):
        """calculate the average Hamming distance between all adjacent chunks of size `chunkSize`
        in `stream`, taken two at a time

        Args:
            stream (str, optional): the stream of bytes (in Hex) to operate on. Defaults to ''.
            chunkSize (int, optional): size of each chunk, in bytes. Defaults to 2.

        Returns:
            float: the average *normalized* Hamming Distance
        """

        chunks = self.getChunks(chunkSize, stream)
        noOfChunks = len(chunks)
        avgDistance = 0
        # take two chunks at a time, so step size = 2
        for i in range(0, noOfChunks, 2):
            j = i + 1
            if j >= noOfChunks:
                break
            chunk1 = chunks[i]
            chunk2 = chunks[j]
            dist = self.byteHamDist(chunk1, chunk2)
            # at most 8 bits can be different i.e, 1 chunkSize = 8 bits
            # so to normalize, divide by max number of bits that can be different
            avgDistance += dist / (8 * chunkSize) # 1 chunkSize = 8 bits
        
        # average all pairs of chunks
        avgDistance /= noOfChunks / 2
        
        return avgDistance
        

# For debugging Hamming Distance of Two Strings
if __name__ == "__main__":
    text1 = input("enter text1: ")
    text2 = input("enter text2: ")
    distance = Toolkit().strHamDist(text1, text2)
    print(f"Distance: { distance }")