# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/?envType=daily-question&envId=2025-11-10
# Minimum Operations to Convert All Elements to Zero

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ans = 0
        stack = [0]

        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                ans += 1
                stack.append(num)

        return ans