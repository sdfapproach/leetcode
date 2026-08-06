# https://leetcode.com/problems/smallest-divisible-digit-product-i/?envType=daily-question&envId=2026-08-06
# Smallest Divisible Digit Product I

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def digit_product(x: int) -> int:
            product = 1

            while x > 0:
                product *= x % 10
                x //= 10

            return product

        while digit_product(n) % t != 0:
            n += 1

        return n