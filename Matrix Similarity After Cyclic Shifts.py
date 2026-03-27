# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/?envType=daily-question&envId=2026-03-27
# Matrix Similarity After Cyclic Shifts

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m, n = len(mat), len(mat[0])
        
        k %= n
        
        for i in range(m):
            if i % 2 == 0:
                shifted = mat[i][k:] + mat[i][:k]
            else:
                shifted = mat[i][-k:] + mat[i][:-k]
            
            if shifted != mat[i]:
                return False
        
        return True