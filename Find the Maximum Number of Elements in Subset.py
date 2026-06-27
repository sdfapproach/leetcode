# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/?envType=daily-question&envId=2026-06-27
# Find the Maximum Number of Elements in Subset

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        ans = 1

        if 1 in cnt:
            if cnt[1] % 2 == 1:
                ans = max(ans, cnt[1])
            else:
                ans = max(ans, cnt[1] - 1)

        for x in list(cnt.keys()):
            if x == 1:
                continue

            length = 0
            cur = x

            while cur in cnt and cnt[cur] >= 2:
                length += 2
                cur = cur * cur

            if cur in cnt:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans