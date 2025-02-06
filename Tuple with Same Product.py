# https://leetcode.com/problems/tuple-with-same-product/?envType=daily-question&envId=2025-02-06
# Tuple with Same Product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        product_counts = {}
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                prod = nums[i] * nums[j]
                product_counts[prod] = product_counts.get(prod, 0) + 1

        result = 0

        for count in product_counts.values():
            if count >= 2:
                result += 8 * (count * (count - 1) // 2)
                
        return result