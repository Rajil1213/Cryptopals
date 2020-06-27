""" Perform XOR on two hex strings """

def main():

    firstVal = input("First Value: ")
    secondVal = input("Second Value: ")
    # convert to decimal
    firstDecimalVal = int(firstVal, base=16)
    secondDecimalVal = int(secondVal, base=16)
    # perform bitwise XOR
    result = firstDecimalVal ^ secondDecimalVal
    # convert to hex and remove the '0x' prefix
    result = hex(result)[2:]
    print(f"XOR Result: { result }")

main()