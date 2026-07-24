# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/?envType=daily-question&envId=2026-07-24
# Number of Unique XOR Triplets II

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        
        max_value = max(nums)

        size = 1 << max_value.bit_length()

        seen = [False] * size
        pair_xor = [False] * size
        triplet_xor = [False] * size

        seen_values = []
        pair_values = []

        for x in nums:
            for y in seen_values:
                value = y ^ x

                if not pair_xor[value]:
                    pair_xor[value] = True
                    pair_values.append(value)

            if not pair_xor[0]:
                pair_xor[0] = True
                pair_values.append(0)

            if not seen[x]:
                seen[x] = True
                seen_values.append(x)

            for value in pair_values:
                triplet_xor[value ^ x] = True

        return sum(triplet_xor)