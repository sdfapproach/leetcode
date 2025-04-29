# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/?envType=daily-question&envId=2025-04-29
# Count Subarrays Where Max Element Appears at Least K Times

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        mx = max(nums)
        n = len(nums)
        ans = cnt = j = 0

        for x in nums:
            while j < n and cnt < k:
                cnt += nums[j] == mx
                j += 1
            if cnt < k:
                break
            ans += n - j + 1
            cnt -= x == mx

        return ans