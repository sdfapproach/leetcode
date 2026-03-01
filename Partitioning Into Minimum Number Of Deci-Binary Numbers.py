# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/?envType=daily-question&envId=2026-03-01
# Partitioning Into Minimum Number Of Deci-Binary Numbers

class Solution:
    def minPartitions(self, n: str) -> int:
        
        return max(map(int, n))