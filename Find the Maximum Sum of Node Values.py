# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/?envType=daily-question&envId=2024-05-19
# Find the Maximum Sum of Node Values

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        maxSum = sum(max(num, num ^ k) for num in nums)
        changedCount = sum((num ^ k) > num for num in nums)

        if changedCount % 2 == 0:
            return maxSum
        
        minChangeDiff = min(abs(num - (num ^ k)) for num in nums)

        return maxSum - minChangeDiff