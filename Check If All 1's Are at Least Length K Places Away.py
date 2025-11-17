# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/?envType=daily-question&envId=2025-11-17
# Check If All 1's Are at Least Length K Places Away

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        last = -10**9

        for i, v in enumerate(nums):
            if v == 1:
                if i - last - 1 < k:
                    return False
                last = i

        return True