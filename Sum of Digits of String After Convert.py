# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/?envType=daily-question&envId=2024-09-03
# Sum of Digits of String After Convert

class Solution:
    def getLucky(self, s: str, k: int) -> int:

        # string = ""

        # for char in s:

        #     string += str(ord(char) - 96)

        # for i in range(k):

        #     num = 0

        #     for char in string:
        #         num += int(char)
            
        #     string = str(num)
        
        # return int(string)

        numeric_string = ''.join(str(ord(char) - 96) for char in s)
    
        for _ in range(k):
            num = sum(int(digit) for digit in numeric_string)
            numeric_string = str(num)
        
        return int(numeric_string)