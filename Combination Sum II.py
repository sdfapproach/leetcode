# https://leetcode.com/problems/combination-sum-ii/?envType=daily-question&envId=2024-08-13
# Combination Sum II

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start, path, target):

            if target == 0:
                result.append(path)
                return

            if target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()
        result = []
        backtrack(0, [], target)

        return result