# https://leetcode.com/problems/compare-version-numbers/?envType=daily-question&envId=2024-05-03
# Compare Version Numbers

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        while v1 and v1[-1] == 0:
            v1.pop()
        while v2 and v2[-1] == 0:
            v2.pop()
        
        max_len = max(len(v1), len(v2))
        v1.extend([0] * (max_len - len(v1)))
        v2.extend([0] * (max_len - len(v2)))
        
        for i in range(max_len):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        
        return 0