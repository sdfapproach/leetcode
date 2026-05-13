# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/?envType=daily-question&envId=2026-05-13
# Minimum Moves to Make Array Complementary

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)

        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            diff[2] += 2

            diff[x + 1] -= 1

            diff[x + y] -= 1
            diff[x + y + 1] += 1

            diff[y + limit + 1] += 1

        ans = float('inf')
        curr = 0

        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            ans = min(ans, curr)

        return ans