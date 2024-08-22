# https://leetcode.com/problems/number-complement/?envType=daily-question&envId=2024-08-22
# Number Complement

class Solution:
    def findComplement(self, num: int) -> int:

        length = num.bit_length()

        return (1 << length) - 1 ^ num