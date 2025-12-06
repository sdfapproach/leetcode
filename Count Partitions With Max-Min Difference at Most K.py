# https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/?envType=daily-question&envId=2025-12-06
# Count Partitions With Max-Min Difference at Most K

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)

        maxq = deque()
        minq = deque()

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[0] = 1
        prefix[0] = 1

        left = 0

        for right in range(n):
            while maxq and nums[maxq[-1]] <= nums[right]:
                maxq.pop()
            maxq.append(right)

            while minq and nums[minq[-1]] >= nums[right]:
                minq.pop()
            minq.append(right)

            while nums[maxq[0]] - nums[minq[0]] > k:
                if maxq[0] == left:
                    maxq.popleft()
                if minq[0] == left:
                    minq.popleft()
                left += 1

            dp[right + 1] = (prefix[right] - (prefix[left - 1] if left > 0 else 0)) % MOD
            prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD

        return dp[n]