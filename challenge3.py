from utils.XOR import AsciiXOR
from sys import argv, exit

def main():
    if len(argv) != 4:
        print("Usage: python3 challenge3.py <ciphertext> <metric> <noOfResults>")
        print("Metrics: pearson chisquare")
        print("noOfResults: 1 - 128")

    noOfResults = int(argv[3]) 
    if not 1 <= noOfResults <= 128:
        print("Displaying Top 15 Results by Default")
        noOfResults = 15

    ciphertext = argv[1]
    decipher = AsciiXOR(ciphertext)

    if argv[2].lower() == 'pearson':
        decipher.pearsonRank(noOfResults)
        exit(0)

    if not argv[2].lower() == 'chisquare':
        print("Using Chisquare Metric By Default")
    
    decipher.chisquareRank(noOfResults)
     

if __name__ == "__main__":
    main()
