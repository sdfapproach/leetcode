# https://leetcode.com/problems/find-missing-and-repeated-values/?envType=daily-question&envId=2025-03-06
# Find Missing and Repeated Values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        flatten = []
        arr = [0] * (len(grid) ** 2)
        answer = [0, 0]

        for li in grid:
            flatten += li

        flatten.sort()

        for n in flatten:

            arr[n-1] += 1

        for i, n in enumerate(arr):
            if n == 2:
                answer[0] = i+1
            elif n == 0:
                answer[1] = i+1

        return answer