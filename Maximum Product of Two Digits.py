# https://leetcode.com/problems/maximum-product-of-two-digits/?envType=daily-question&envId=2026-07-25
# Maximum Product of Two Digits

class Solution:
    def maxProduct(self, n: int) -> int:

        max_product = 0
        
        for i, num1 in enumerate(str(n)):

            for num2 in str(n)[i+1:]:

                max_product = max(max_product, int(num1) * int(num2))

        return max_product
