# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/?envType=daily-question&envId=2026-11-13
# Count Non-Decreasing Subarrays After K Operations

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        dq = deque()
        right = n - 1
        cost = 0
        answer = 0

        for left in range(n - 1, -1, -1):

            while dq and nums[dq[-1]] < nums[left]:
                idx = dq.pop()

                end = dq[-1] if dq else right + 1

                cost += (
                    nums[left] - nums[idx]
                ) * (end - idx)

            dq.append(left)

            while cost > k:
                cost -= nums[dq[0]] - nums[right]

                if dq[0] == right:
                    dq.popleft()

                right -= 1

            answer += right - left + 1

        return answer