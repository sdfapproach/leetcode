# https://leetcode.com/problems/maximum-swap/?envType=daily-question&envId=2024-10-17
# Maximum Swap

class Solution:
    def maximumSwap(self, num: int) -> int:

        num = list(str(num))
        last_occurrence = {int(n): i for i, n in enumerate(num)}
        
        for i, n in enumerate(num):
            for d in range(9, int(n), -1):
                if last_occurrence.get(d, -1) > i:
                    num[i], num[last_occurrence[d]] = num[last_occurrence[d]], num[i]
                    return int("".join(num))
        
        return int("".join(num))