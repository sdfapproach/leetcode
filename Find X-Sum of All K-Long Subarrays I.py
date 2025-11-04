# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/?envType=daily-question&envId=2025-11-04
# Find X-Sum of All K-Long Subarrays I

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        n = len(nums)
        freq = Counter()
        result = []

        for i in range(k):
            freq[nums[i]] += 1

        def x_sum():
            top = sorted(freq.items(), key=lambda p: (-p[1], -p[0]))
            total = 0
            count = 0
            for val, f in top:
                if count >= x:
                    break
                total += val * f
                count += 1
            return total

        result.append(x_sum())

        for i in range(k, n):
            left = nums[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            freq[nums[i]] += 1
            result.append(x_sum())

        return result