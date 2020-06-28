import os
from utils.XOR import AsciiXOR

def main():

    directory = 'files'
    filename = '4.txt'
    path = os.path.join(directory, filename)
    with open(path, 'r') as txt:
        ciphers = txt.readlines() 

    scores = []
    texts = []
    for cipher in ciphers:
        # remove the trailing whitespace(newline) and initialize AsciiXOR with it
        decode = AsciiXOR(cipher.rstrip())
        # get the top result of deciphering => (text, score)
        result = decode.chisquareRank(get=True)
        text = result[0]
        score = result[1]
        texts.append(text)
        scores.append(score)
    
    # sort the texts according to their scores
    ranking = [ (text, score) for (score, text) in sorted(zip(scores, texts))]

    print("Top 10 Lines:")
    noOfLines = 10
    for i in range(noOfLines):
        textVal = ranking[i][0]
        scoreVal = ranking[i][1]
        lineVal = scores.index(scoreVal) + 1
        print(f"Rank: #{ i+1 }, Line: { lineVal }")
        print(f"Text: { textVal }, Score: { scoreVal }")

if __name__ == "__main__":
    main()
