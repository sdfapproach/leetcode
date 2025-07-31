# https://leetcode.com/problems/bitwise-ors-of-subarrays/?envType=daily-question&envId=2025-07-31
# Bitwise ORs of Subarrays

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        
        prev = set()
        res = set()

        for v in arr:
            curr = {v}
            for x in prev:
                curr.add(x | v)
            res |= curr
            prev = curr

        return len(res)