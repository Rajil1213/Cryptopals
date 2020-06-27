import re
from string import punctuation
from sys import argv, exit
from scipy import std
from scipy.stats import pearsonr

FREQUENCY_TABLE = {'a':8.497, 'b': 1.492, 'c': 2.202, 'd': 4.253, 'e': 11.162, \
        'f': 2.228, 'g': 2.015,	'h': 6.094, 'i': 7.546,	'j': 0.153,	'k': 1.292, \
        'l': 4.025, 'm': 2.406,	'n': 6.749,	'o': 7.507,	'p': 1.929, 'q': 0.095, \
        'r': 7.587, 's': 6.327,	't': 9.356,	'u': 2.758,	'v': 0.978,	'w': 2.560,	\
        'x': 0.150, 'y': 1.994, 'z': 0.077 }


def byteXOR(ciphertext, key):

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

def scoreText(text):

    frequency_count = { key: 0 for key in FREQUENCY_TABLE }
    letters = []
    punctuationCount = 0
    for letter in text:
        if letter.isalpha():
            letters.append(letter.lower())
            continue
        if letter in punctuation:
            punctuationCount += 1

    if punctuationCount > len(letters):
        return 0
    
    noOfLetters = len(text) - punctuationCount
    if noOfLetters == 0:
        return 0

    for letter in letters:
        frequency_count[letter] += 1
    
    frequency_count = { key: 100 * value / noOfLetters \
        for (key, value) in frequency_count.items()}
    
    present = []
    required = []
    for letter in FREQUENCY_TABLE:
        present.append(frequency_count[letter])
        required.append(FREQUENCY_TABLE[letter])

    if std(present) <= 2:
        return 0

    score, _ = pearsonr(present, required)

    return score
    

def main():

    if not len(argv) == 2:
        print("Usage python3 challenge3.py <ciphertext>")
        exit(1)

    ciphertext = argv[1]
    asciiRange = 128
    scores = []
    texts = []
    for i in range(asciiRange):
        text = byteXOR(ciphertext, i)
        score = scoreText(text)
        scores.append(score)
        texts.append(text)
    
    noOfResults = 20
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
       

if __name__ == "__main__":
    main()
