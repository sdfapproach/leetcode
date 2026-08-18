# https://leetcode.com/problems/find-the-largest-almost-missing-integer/?envType=daily-question&envId=2026-08-18
# Find the Largest Almost Missing Integer

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        count = defaultdict(int)
        n = len(nums)

        for i in range(n - k + 1):
            window = set(nums[i:i + k])

            for x in window:
                count[x] += 1

        answer = -1

        for x, c in count.items():
            if c == 1:
                answer = max(answer, x)

        return answer