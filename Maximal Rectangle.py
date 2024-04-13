# https://leetcode.com/problems/maximal-rectangle/?envType=daily-question&envId=2024-04-13
# Maximal Rectangle

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        heights = [0] * (len(matrix[0]) + 1)

        for row in matrix:
            for i in range(len(matrix[0])):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            stack = []
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area