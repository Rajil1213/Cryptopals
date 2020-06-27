from sys import exit

class BinaryOps:

    @classmethod
    def xor(cls, arg1, arg2):
        """performs bitwise XOR on bits of arg1 and arg2

        Args:
            arg1 (string): first operand
            arg2 (string): second operand

        Returns:
            string: the result of `arg1` bitwise-XOR `arg2`
        """

        if not len(arg1) == len(arg2):
            print("Bit lengths of arguments not equal")
            print(f"{ len(arg1) } != { len(arg2) }")
            exit(1)

        result = ""
        n = len(arg1)
        for i in range(n):

            bit1 = arg1[i]
            bit2 = arg2[i]

            if bit1 == bit2:
                value = '0'
            else:
                value = '1'
            
            result += value
        
        return result



