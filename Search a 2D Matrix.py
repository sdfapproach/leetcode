# https://leetcode.com/problems/search-a-2d-matrix/
# Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_matrix = []

        for m in matrix:
            new_matrix += m

        if target in new_matrix:
            return True
        else:
            return False