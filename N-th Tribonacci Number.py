# https://leetcode.com/problems/n-th-tribonacci-number/?envType=daily-question&envId=2024-04-24
# N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:

        # tribo = [0, 1, 1]

        # for i in range(3, n+1):
        #     tribo.append(tribo[i-1] + tribo[i-2] + tribo[i-3])

        # return tribo[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1

        for _ in range(3, n+1):
            a, b, c = b, c, a + b + c
        
        return c