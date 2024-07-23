# https://leetcode.com/problems/sort-array-by-increasing-frequency/?envType=daily-question&envId=2024-07-23
# Sort Array by Increasing Frequency

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        freq = Counter(nums)

        return sorted(nums, key = lambda x : (freq[x], -x))