# https://leetcode.com/problems/the-number-of-beautiful-subsets/description/?envType=daily-question&envId=2024-05-23
# The Number of Beautiful Subsets

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        cnt = Counter()
        
        def backtrack(index):
            if index == len(nums):
                return 1
            
            total = 0
            
            total += backtrack(index + 1)
            
            if cnt[nums[index] - k] == 0:
                cnt[nums[index]] += 1
                total += backtrack(index + 1)
                cnt[nums[index]] -= 1
            
            return total
        
        return backtrack(0) - 1