from math import inf
import re
from string import punctuation
from scipy import std
from scipy.stats import pearsonr

class AsciiXOR:
    """performs some XOR encryption and decryption on texts, and also ranks results
    based on the Karl-Pearson and/or the Chi-Squared Metric

    Returns:
        AsciiXOR: an object of this class with `self.ciphertext` = passed_in_argument
    """

    # source: https://en.wikipedia.org/wiki/Letter_frequency
    # accessed: Jun 28, 2020
    FREQUENCY_TABLE = {'a': 8.497, 'b': 1.492, 'c': 2.202, 'd': 4.253, 'e': 11.162, \
        'f': 2.228, 'g': 2.015,	'h': 6.094, 'i': 7.546,	'j': 0.153,	'k': 1.292, \
        'l': 4.025, 'm': 2.406,	'n': 6.749,	'o': 7.507,	'p': 1.929, 'q': 0.095, \
        'r': 7.587, 's': 6.327,	't': 9.356,	'u': 2.758,	'v': 0.978,	'w': 2.560,	\
        'x': 0.150, 'y': 1.994, 'z': 0.077 }

    ciphertext = ""

    def __init__(self, cipher):
       self.ciphertext = cipher

    def singleByteXOR(self, key):
        """perform single-byte XOR with `key`

        Args:
            key (int): an ascii value 0-127

        Returns:
            str: a plain-text string obtained by single-byte XOR-ing `self.ciphertext` with `key`
        """

        ciphertext = self.ciphertext
        n = len(ciphertext)
        result = ""
        for i in range(0, n, 2):
            # perform operation on 2 hex values = 2 nibbles = 1 byte at a time
            byte = ciphertext[i:i+2]
            # convert hex to decimal
            byteDecimal = int(byte, base=16)
            # perform xor and convert to ascii equivalent character
            output = byteDecimal ^ key
            character = chr(output)
            # remove any non-printable characters with ascii values 00 to 1f
            prettyCharacter = re.sub("[\x00-\x1f]", "", character) 
            result += prettyCharacter
            
        return result
    
    
    def repeatKeyXOR(self, key):
        """performs repeat-key XOR on `self.ciphertext` with `key`

        Args:
            key (str): a string that hold the ciphering key

        Returns:
            str: a string obtained by repeat-key XORing `self.ciphertext` with `key`
        """
        ciphertext = self.ciphertext
        n = len(ciphertext)
        keyLength = len(key)
        result = ""
        for i in range(0, n, 2):
            # key is a human-readable string, advance 1 byte = 1 character at a time
            keyIndex = i // 2
            # get 1 byte = 2 hex values from the ciphertext
            byte = ciphertext[i:i+2]
            # convert 'byte' from hex to decimal
            byteDecimal = int(byte, base=16)
            # perform XOR with a character of the `key`, wrap it around with module `keyLength`
            output = byteDecimal ^ key[keyIndex % keyLength]
            # change decimal to equivalent ASCII character
            character = chr(output)
            # remove non-printable ASCII characters with values 00 to 1F
            prettyCharacter = re.sub("[\x00-\x1f]", "", character) 
            result += prettyCharacter
            
        return result


    def scoreTextChisquare(self, text):
        """scores a piece of text using Chi-Squared Metric

        Args:
            text (str): a string that holds the piece of text

        Returns:
            float: the score based on the Chi-Squared Metric
        """
        # initialize frequencies to 0
        frequency_count = { key: 0 for key in self.FREQUENCY_TABLE }
        letters = []
        punctuationCount = 0
        for letter in text:
            # only get alphabets, convert to lowercase
            if letter.isalpha():
                letters.append(letter.lower())
            # get number of punctuations
            if letter in punctuation:
                punctuationCount += 1

        noOfLetters = len(letters)   
        # too many punctuations? or, no letters?
        # then score = maximum (worst)
        if punctuationCount >= noOfLetters or noOfLetters == 0:
            return inf

        # calculate the frequency percentage for each letter
        for letter in letters:
            frequency_count[letter] += 100 / noOfLetters

        # get the Chi-square score
        score = 0 
        for letter in self.FREQUENCY_TABLE:
            
            observed = frequency_count[letter]
            actual = self.FREQUENCY_TABLE[letter]

            numerator = (observed - actual) ** 2
            score += numerator / actual
        
        return score
        
    
    def scoreTextPearson(self, text):
        """scores a piece of text based on the Karl-Peasron Metric

        Args:
            text (str): a string that holds a piece of text

        Returns:
            float: the Karl-Person Correlation Coefficient for `text`'s character frequencies and
            the actual character frequencies for the English language
        """
        # initialize frequencies to 0 
        frequency_count = { key: 0 for key in self.FREQUENCY_TABLE }
        letters = []
        punctuationCount = 0
        for letter in text:
            # get only the alphabets, convert to lowercase 
            if letter.isalpha():
                letters.append(letter.lower())
                continue
            # count the punctuations    
            if letter in punctuation:
                punctuationCount += 1

        noOfLetters = len(text)  
        # if there are no letters or more punctuations than letters
        # score = minimum (0, worst)
        if noOfLetters == 0 or punctuationCount >= noOfLetters:
            return 0

        # get frequency percentage for each letter
        for letter in letters:
            frequency_count[letter] += 100 / noOfLetters
        
        # calculate the list of observed and actual frequencies
        observed = []
        actual = []
        for letter in self.FREQUENCY_TABLE:
            observed.append(frequency_count[letter])
            actual.append(self.FREQUENCY_TABLE[letter])

        # for English language, standard deviation > 3
        # if the observed standard deviationi <= 2, score = 0 
        if std(observed) <= 2:
            return 0

        # get the Karl Pearons' Correlation Coefficient
        score, _ = pearsonr(observed, actual)

        return score
        

    def pearsonRank(self, noOfResults=15):
        """Displays top `noOfResults` for plaintext based on the Karl-Pearson metric

        Args:
            noOfResults (int, optional): the number of results to display. Defaults to 15.
        """

        scores = []
        texts = []
        for i in range(128):
            text = self.singleByteXOR(i)
            score = self.scoreTextPearson(text)
            scores.append(score)
            texts.append(text)

        print(f"Top { noOfResults } Results: ")
        # sort the texts based on their scores in *descending* order
        # higher value of Karl Pearson Coefficient = better result
        topResults = [(txt, scr) for scr, txt in sorted(zip(scores, texts))]
        topResults.reverse()
        for index in range(noOfResults):
            rank = index + 1
            plaintext = topResults[index][0]
            score = topResults[index][1]
            ascii = texts.index(plaintext)
            key = chr(ascii)
            print(f"Rank: #{ rank }, Key: { key }, ASCII: { ascii }, Score: { score }")
            print(f"Plaintext: { plaintext }")
        

    def chisquareRank(self, noOfResults=15):
        """displays the top `noOfResults` for plaintext based on the Chi-Squared Metric

        Args:
            noOfResults (int, optional): the number of results to display. Defaults to 15.
        """

        scores = []
        texts = []
        for i in range(128):
            text = self.singleByteXOR(i)
            score = self.scoreTextChisquare(text)
            scores.append(score)
            texts.append(text)
        
        print(f"Top { noOfResults } Results: ")
        # sort texts based on their scores, in *ascending* order
        # lower the Chi-Squared Metric score = better the result
        topResults = [(txt, scr) for scr, txt in sorted(zip(scores, texts))]
        for index in range(noOfResults):
            rank = index + 1
            plaintext = topResults[index][0]
            score = topResults[index][1]
            ascii = texts.index(plaintext)
            key = chr(ascii)
            print(f"Rank: #{ rank }, Key: { key }, ASCII: { ascii }, Score: { score }")
            print(f"Plaintext: { plaintext }")
