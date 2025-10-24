# https://leetcode.com/problems/next-greater-numerically-balanced-number/?envType=daily-question&envId=2025-10-24
# Next Greater Numerically Balanced Number

class Solution(object):
    def nextBeautifulNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isBalance(num):
            count = [0] * 10
            while num > 0:
                if num % 10 == 0:
                    return False
                count[num % 10] += 1
                num //= 10
            return all(c == i for i, c in enumerate(count) if c)

        n += 1
        while not isBalance(n):
            n += 1
        return n