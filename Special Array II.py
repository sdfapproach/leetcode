# https://leetcode.com/problems/special-array-ii/?envType=daily-question&envId=2024-12-09
# Special Array II

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        n = len(nums)
        is_special_prefix = [0] * (n + 1)

        for i in range(1, n):
            if (nums[i - 1] % 2) != (nums[i] % 2):
                is_special_prefix[i] = is_special_prefix[i - 1] + 1
            else:
                is_special_prefix[i] = is_special_prefix[i - 1]

        result = []

        for fromi, toi in queries:
            special_count = is_special_prefix[toi] - is_special_prefix[fromi]
            if special_count == (toi - fromi):
                result.append(True)
            else:
                result.append(False)

        return result