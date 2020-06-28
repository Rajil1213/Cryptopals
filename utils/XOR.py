from math import inf
import re
from string import punctuation
from scipy import std
from scipy.stats import pearsonr

class AsciiXOR:

    FREQUENCY_TABLE = {'a': 8.497, 'b': 1.492, 'c': 2.202, 'd': 4.253, 'e': 11.162, \
        'f': 2.228, 'g': 2.015,	'h': 6.094, 'i': 7.546,	'j': 0.153,	'k': 1.292, \
        'l': 4.025, 'm': 2.406,	'n': 6.749,	'o': 7.507,	'p': 1.929, 'q': 0.095, \
        'r': 7.587, 's': 6.327,	't': 9.356,	'u': 2.758,	'v': 0.978,	'w': 2.560,	\
        'x': 0.150, 'y': 1.994, 'z': 0.077 }

    ciphertext = ""

    def __init__(self, cipher):
       self.ciphertext = cipher

    def singleByteXOR(self, key):

        ciphertext = self.ciphertext
        n = len(ciphertext)
        result = ""
        for i in range(0, n, 2):
            byte = ciphertext[i:i+2]
            byteDecimal = int(byte, base=16)
            output = byteDecimal ^ key
            character = chr(output)
            prettyCharacter = re.sub("[\x00-\x1f]", "", character) 
            result += prettyCharacter
            
        return result
    
    
    def repeatKeyXOR(self, key):

        ciphertext = self.ciphertext
        n = len(ciphertext)
        keyLength = len(key)
        result = ""
        for i in range(0, n, 2):
            keyIndex = i // 2
            byte = ciphertext[i:i+2]
            byteDecimal = int(byte, base=16)
            output = byteDecimal ^ key[keyIndex % keyLength]
            character = chr(output)
            prettyCharacter = re.sub("[\x00-\x1f]", "", character) 
            result += prettyCharacter
            
        return result


    def scoreTextChisquare(self, text):
        
        frequency_count = { key: 0 for key in self.FREQUENCY_TABLE }
        letters = []
        punctuationCount = 0
        for letter in text:
            if letter.isalpha():
                letters.append(letter.lower())
            if letter in punctuation:
                punctuationCount += 1

        noOfLetters = len(letters)   
        if punctuationCount >= noOfLetters or noOfLetters == 0:
            return inf

        for letter in letters:
            frequency_count[letter] += 100 / noOfLetters

        score = 0 
        for letter in self.FREQUENCY_TABLE:
            
            observed = frequency_count[letter]
            actual = self.FREQUENCY_TABLE[letter]

            numerator = (observed - actual) ** 2
            score += numerator / actual
        
        return score
        
    
    def scoreTextPearson(self, text):

        frequency_count = { key: 0 for key in self.FREQUENCY_TABLE }
        letters = []
        punctuationCount = 0
        for letter in text:
            if letter.isalpha():
                letters.append(letter.lower())
                continue
            if letter in punctuation:
                punctuationCount += 1

        noOfLetters = len(text)  
        if noOfLetters == 0:
            return 0

        if punctuationCount > len(letters):
            return 0

        for letter in letters:
            frequency_count[letter] += 100 / noOfLetters
        
        observed = []
        actual = []
        for letter in self.FREQUENCY_TABLE:
            observed.append(frequency_count[letter])
            actual.append(self.FREQUENCY_TABLE[letter])

        if std(observed) <= 2:
            return 0

        score, _ = pearsonr(observed, actual)

        return score
        

    def pearsonRank(self, noOfResults=15):

        scores = []
        texts = []
        for i in range(128):
            text = self.singleByteXOR(i)
            score = self.scoreTextPearson(text)
            scores.append(score)
            texts.append(text)

        print(f"Top { noOfResults } Results: ")
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

        scores = []
        texts = []
        for i in range(128):
            text = self.singleByteXOR(i)
            score = self.scoreTextChisquare(text)
            scores.append(score)
            texts.append(text)
        
        print(f"Top { noOfResults } Results: ")
        topResults = [(txt, scr) for scr, txt in sorted(zip(scores, texts))]
        for index in range(noOfResults):
            rank = index + 1
            plaintext = topResults[index][0]
            score = topResults[index][1]
            ascii = texts.index(plaintext)
            key = chr(ascii)
            print(f"Rank: #{ rank }, Key: { key }, ASCII: { ascii }, Score: { score }")
            print(f"Plaintext: { plaintext }")
