# https://leetcode.com/problems/sum-of-all-subset-xor-totals/?envType=daily-question&envId=2024-05-20
# Sum of All Subset XOR Totals

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def helper(idx, current_xor):
            nonlocal total
            if idx == len(nums):
                total += current_xor
                return

            helper(idx + 1, current_xor ^ nums[idx])
            helper(idx + 1, current_xor)
        
        total = 0
        helper(0, 0)
        return total