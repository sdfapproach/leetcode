# https://leetcode.com/problems/count-number-of-nice-subarrays/?envType=daily-question&envId=2024-06-22
# Count Number of Nice Subarrays

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        odd_indices = [-1]

        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_indices.append(i)

        odd_indices.append(len(nums))

        nice_subarrays_count = 0
        
        for i in range(1, len(odd_indices) - k):
            start = odd_indices[i - 1] + 1
            end = odd_indices[i + k] - 1
            left_choices = odd_indices[i] - start + 1
            right_choices = end - odd_indices[i + k - 1] + 1
            nice_subarrays_count += left_choices * right_choices

        return nice_subarrays_count