# https://leetcode.com/problems/ugly-number-ii/?envType=daily-question&envId=2024-08-18
# Ugly Number II

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        # ugly = 0
        # count = 0
        # i = 1

        # while count < n:

        #     num = i

        #     for p in [2, 3, 5]:
        #         while num % p == 0:
        #             num //= p
        #     if num == 1:
        #         count += 1
        #         ugly = i
        #     i += 1

        # return ugly


        ugly_numbers = [0] * n
        ugly_numbers[0] = 1
        
        i2 = i3 = i5 = 0
        
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        
        for i in range(1, n):
            ugly_numbers[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            
            if ugly_numbers[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly_numbers[i2] * 2
            
            if ugly_numbers[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly_numbers[i3] * 3
            
            if ugly_numbers[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly_numbers[i5] * 5
        
        return ugly_numbers[-1]