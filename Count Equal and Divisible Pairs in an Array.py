# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/?envType=daily-question&envId=2025-04-17
# Count Equal and Divisible Pairs in an Array

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        index_map = defaultdict(list)
    
        for i, num in enumerate(nums):
            index_map[num].append(i)
        
        count = 0
        
        for indices in index_map.values():
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    if (indices[i] * indices[j]) % k == 0:
                        count += 1
                        
        return count