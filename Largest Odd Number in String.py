# https://leetcode.com/problems/largest-odd-number-in-string/description/?envType=daily-question&envId=2023-12-07
# 1903. Largest Odd Number in String

#class Solution:
#    def largestOddNumber(self, num: str) -> str:
#        num = list(num)
#        odd_num = ""

#        for i, n in enumerate(reversed(num)):
#            if int(n)%2 != 0:
#                odd_num = num[:len(num)-i]
#                break

#        return "".join(odd_num)

class Solution:
    def largestOddNumber(self, num: str) -> str:
        num = list(reversed(num))
        odd_num = []

        for n in num:
            if int(n) % 2 != 0:
                odd_num.append(n)
            else:
                break

        return "".join(reversed(odd_num))
