# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/?envType=daily-question&envId=2026-03-22
# Determine Whether Matrix Can Be Obtained By Rotation

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate(matrix):
            n = len(matrix)
            return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
        
        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        
        return False