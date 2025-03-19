# https://leetcode.com/problems/alternating-groups-ii/?envType=daily-question&envId=2025-03-09
# Alternating Groups II

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        # arr = colors + colors[:k-1]

        # count = 0

        # def alternating(group):

        #     for i in range(1, len(group)):
        #         if group[i] == group[i-1]:
        #             return False
            
        #     return True


        # for i in range(len(colors)):
        #     if alternating(arr[i:k+i]):
        #         count += 1

        # return count

        n = len(colors)
        if k == 1:
            return n

        ext = colors + colors[:k-1]
        m = len(ext)
        
        diff = [0] * (m - 1)
        for i in range(m - 1):
            if ext[i] == ext[i + 1]:
                diff[i] = 1
        
        prefix = [0] * (m)
        for i in range(m - 1):
            prefix[i + 1] = prefix[i] + diff[i]
        
        count = 0
        for i in range(n):
            if prefix[i + k - 1] - prefix[i] == 0:
                count += 1

        return count