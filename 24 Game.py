# https://leetcode.com/problems/24-game/?envType=daily-question&envId=2025-08-18
# 24 Game

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        
        EPS = 1e-6


        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    a, b = nums[i], nums[j]
                    rest = [nums[k] for k in range(n) if k != i and k != j]
                    candidates = set()
                    candidates.add(a + b)
                    candidates.add(a - b)
                    candidates.add(b - a)
                    candidates.add(a * b)
                    if abs(b) > EPS: candidates.add(a / b)
                    if abs(a) > EPS: candidates.add(b / a)
                    for v in candidates:
                        if dfs(rest + [v]):
                            return True
            return False

        return dfs([float(x) for x in cards])