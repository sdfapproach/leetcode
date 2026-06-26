# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/?envType=daily-question&envId=2026-06-26
# Count Subarrays With Majority Element II

class Fenwick:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def add(self, i, v):
        i += 1
        while i < len(self.tree):
            self.tree[i] += v
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        offset = n + 1
        size = 2 * n + 3

        bit = Fenwick(size)

        prefix = 0
        ans = 0

        bit.add(prefix + offset, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.sum(prefix + offset - 1)

            bit.add(prefix + offset, 1)

        return ans