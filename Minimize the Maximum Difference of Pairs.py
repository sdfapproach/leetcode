# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/?envType=daily-question&envId=2025-06-13
# Minimize the Maximum Difference of Pairs

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        n = len(nums)
        if p == 0:
            return 0

        nums.sort()

        def can(mid: int) -> bool:
            cnt = 0
            i = 1
            while i < n and cnt < p:
                if nums[i] - nums[i - 1] <= mid:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        left, right = 0, nums[-1] - nums[0]
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer