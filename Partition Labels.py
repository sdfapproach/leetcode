# https://leetcode.com/problems/partition-labels/?envType=daily-question&envId=2025-03-30
# Partition Labels

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_occ = {c: i for i, c in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, last_occ[c])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        
        return partitions