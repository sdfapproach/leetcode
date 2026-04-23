# https://leetcode.com/problems/sum-of-distances/?envType=daily-question&envId=2026-04-23
# Sum of Distances

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        n = len(nums)
        res = [0] * n
        
        for indices in pos.values():
            prefix_sum = [0]
            
            for x in indices:
                prefix_sum.append(prefix_sum[-1] + x)
            
            m = len(indices)
            
            for k in range(m):
                x = indices[k]
                left = x * k - prefix_sum[k]
                right = (prefix_sum[m] - prefix_sum[k+1]) - x * (m - k - 1)
                res[x] = left + right
        
        return res