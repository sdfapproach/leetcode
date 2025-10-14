# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/?envType=daily-question&envId=2025-10-14
# Adjacent Increasing Subarrays Detection I

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)

        if k == 1:
            return n >= 2
        if 2 * k > n:
            return False

        inc = [1 if nums[i] < nums[i+1] else 0 for i in range(n-1)]
        pref = [0]

        for x in inc:
            pref.append(pref[-1] + x)

        for a in range(0, n - 2*k + 1):
            ok1 = (pref[a + k - 1] - pref[a]) == (k - 1)
            ok2 = (pref[a + 2*k - 1] - pref[a + k]) == (k - 1)

            if ok1 and ok2:
                return True

        return False