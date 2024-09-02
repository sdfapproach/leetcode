# https://leetcode.com/problems/convert-1d-array-into-2d-array/?envType=daily-question&envId=2024-09-01
# Convert 1D Array Into 2D Array

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if len(original) != m * n:
            return []
        
        return [original[i*n:(i+1)*n] for i in range(m)]