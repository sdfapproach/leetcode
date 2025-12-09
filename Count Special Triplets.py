# https://leetcode.com/problems/count-special-triplets/?envType=daily-question&envId=2025-12-09
# Count Special Triplets

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        
        right = Counter(nums)
        left = Counter()

        answer = 0
        
        for j, val in enumerate(nums):
            right[val] -= 1
            target = val * 2
            
            answer = (answer + left[target] * right[target]) % MOD
            
            left[val] += 1
        
        return answer