# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/?envType=daily-question&envId=2025-05-03
# Minimum Domino Rotations For Equal Row

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def check(target):
            rotations_top = rotations_bottom = 0
            
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                
                if tops[i] != target:
                    rotations_top += 1
                
                if bottoms[i] != target:
                    rotations_bottom += 1
            
            return min(rotations_top, rotations_bottom)
        
        result = float('inf')

        for target in range(1, 7):
            rotations = check(target)
            if rotations != -1:
                result = min(result, rotations)
        
        return result if result != float('inf') else -1