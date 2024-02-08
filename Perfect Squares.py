# https://leetcode.com/problems/perfect-squares/?envType=daily-question&envId=2024-02-08
# Perfect Squares

class Solution:
    def numSquares(self, n: int) -> int:
        
        # squares = []

        # dp = []

        # for i in range(2, n):
        #     if i**2 > n:
        #         break
        #     squares.append(i**2)

        
        # for n in squares[::-1]:

        #     num = n

        #     while num > 0:
        #         num %= n
        #     print(n)


        # return 0

        dp = [n+1] * (n+1)
        dp[0] = 0

        squares = [i**2 for i in range(1, int(n**0.5) + 1)]

        for i in range(1, n+1):
            for square in squares:
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
                else:
                    break

        return dp[n]