# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/?envType=daily-question&envId=2025-10-22
# Maximum Frequency of an Element After Performing Operations II

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        
        ans = 1
        adjustable = 0
        count = collections.Counter(nums)
        line = SortedDict()
        candidates = set()

        for num in nums:
            line[num - k] = line.get(num - k, 0) + 1
            line[num + k + 1] = line.get(num + k + 1, 0) - 1
            candidates.add(num)
            candidates.add(num - k)
            candidates.add(num + k + 1)

        for num in sorted(candidates):
            adjustable += line.get(num, 0)
            adjusted = adjustable - count[num]
            ans = max(ans, count[num] + min(numOperations, adjusted))

        return ans