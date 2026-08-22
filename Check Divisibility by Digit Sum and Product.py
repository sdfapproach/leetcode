# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/?envType=daily-question&envId=2026-08-22
# Check Divisibility by Digit Sum and Product

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        num = [int(n) for n in list(str(n))]
        
        digit_sum = reduce(lambda x,y:x+y, num)
        digit_product = reduce(lambda x,y:x*y, num)

        if n % (digit_sum + digit_product) == 0:
            return True
        else:
            return False