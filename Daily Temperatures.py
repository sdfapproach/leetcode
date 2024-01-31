# https://leetcode.com/problems/daily-temperatures/?envType=daily-question&envId=2024-01-31
# Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_index = stack.pop()
                arr[prev_index] = i - prev_index
            stack.append(i)

        return arr