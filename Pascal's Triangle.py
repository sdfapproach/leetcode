# https://leetcode.com/problems/pascals-triangle/?envType=daily-question&envId=2025-08-01
# Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        else:
            tri = [[1]]
            for i in range(2, numRows+1):

                arr = [1]
                for j in range(1, i-1):
                    arr.append(tri[-1][j-1]+tri[-1][j])
                arr.append(1)
                tri.append(arr)

            return tri