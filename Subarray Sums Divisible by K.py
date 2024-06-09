# https://leetcode.com/problems/subarray-sums-divisible-by-k/?envType=daily-question&envId=2024-06-09
# Subarray Sums Divisible by K

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count = 0
        cumulative_sum = 0
        remainder_freq = {0: 1}

        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k

            if remainder < 0:
                remainder += k

            if remainder in remainder_freq:
                count += remainder_freq[remainder]

            if remainder in remainder_freq:
                remainder_freq[remainder] += 1
            else:
                remainder_freq[remainder] = 1

        return count