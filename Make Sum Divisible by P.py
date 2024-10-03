# https://leetcode.com/problems/make-sum-divisible-by-p/?envType=daily-question&envId=2024-10-03
# Make Sum Divisible by P

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total_sum = sum(nums)
        target = total_sum % p

        if target == 0:
            return 0

        n = len(nums)
        prefix_sum = 0
        min_len = n
        prefix_mod_map = {0: -1}

        for i in range(n):
            prefix_sum += nums[i]
            mod = prefix_sum % p
            
            needed_mod = (mod - target) % p
            if needed_mod in prefix_mod_map:
                min_len = min(min_len, i - prefix_mod_map[needed_mod])
            
            prefix_mod_map[mod] = i

        return min_len if min_len < n else -1