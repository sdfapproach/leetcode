# https://leetcode.com/problems/subarrays-with-k-different-integers/?envType=daily-question&envId=2024-03-30
# Subarrays with K Different Integers

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        # sub_list_count = 0

        # for i in range(len(nums)):

        #     count = 0
        #     sub_list = []
        #     j = i

        #     for j in range(len(nums[i:])):

        #         if nums[i:][j] not in sub_list:
        #             sub_list.append(nums[i:][j])
        #             count += 1

        #         if count == k:
        #             sub_list_count += 1
        #         elif count > k:
        #             continue

        # return sub_list_count

        def at_most_k(nums, k):
            count = 0
            start = 0
            freq = {}
            for end in range(len(nums)):
                if nums[end] not in freq or freq[nums[end]] == 0:
                    k -= 1
                freq[nums[end]] = freq.get(nums[end], 0) + 1
                
                while k < 0:
                    freq[nums[start]] -= 1
                    if freq[nums[start]] == 0:
                        k += 1
                    start += 1
                
                count += end - start + 1
            return count

        return at_most_k(nums, k) - at_most_k(nums, k - 1)