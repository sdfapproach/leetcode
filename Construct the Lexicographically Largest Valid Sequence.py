# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/?envType=daily-question&envId=2025-02-16
# Construct the Lexicographically Largest Valid Sequence

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:

        ans = [0] * (2 * n - 1)
        visited = [False] * (n + 1)
        
        def backtrack(index: int) -> bool:
            if index == len(ans):
                return True
            if ans[index] != 0:
                return backtrack(index + 1)
            
            for num in range(n, 0, -1):
                if visited[num]:
                    continue
                if num == 1:
                    ans[index] = 1
                    visited[1] = True
                    if backtrack(index + 1):
                        return True
                    ans[index] = 0
                    visited[1] = False
                else:
                    if index + num < len(ans) and ans[index] == 0 and ans[index + num] == 0:
                        ans[index] = num
                        ans[index + num] = num
                        visited[num] = True
                        if backtrack(index + 1):
                            return True
                        ans[index] = 0
                        ans[index + num] = 0
                        visited[num] = False
            return False
        
        backtrack(0)
        return ans