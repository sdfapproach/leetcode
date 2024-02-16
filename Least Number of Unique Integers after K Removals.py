# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/?envType=daily-question&envId=2024-02-16
# Least Number of Unique Integers after K Removals

from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # count = Counter(arr)

        # integers = [n for n in count.values()]

        # integers.sort()

        # i = 0
        # while k > 0:
        #     g = integers[i] - k 
        #     k -= integers[i]
        #     integers[i] = g
        #     i += 1

        # return len([n for n in integers if n > 0])

        count = Counter(arr)
        frequencies = list(count.values())
        
        frequencies.sort()
        
        for i, freq in enumerate(frequencies):
            if k <= 0:
                break
            k -= freq
            if k < 0:
                frequencies[i] = -k
            else:
                frequencies[i] = 0
        
        return sum(freq > 0 for freq in frequencies)