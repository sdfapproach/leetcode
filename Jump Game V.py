# https://leetcode.com/problems/jump-game-v/?envType=daily-question&envId=2026-05-24
# Jump Game V

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        n = len(arr)

        memo = [0] * n

        def dfs(i):

            if memo[i] != 0:

                return memo[i]

            best = 1

            for j in range(i + 1, min(n, i + d + 1)):

                if arr[j] >= arr[i]:

                    break

                best = max(best, 1 + dfs(j))

            for j in range(i - 1, max(-1, i - d - 1), -1):

                if arr[j] >= arr[i]:

                    break

                best = max(best, 1 + dfs(j))

            memo[i] = best

            return best

        return max(dfs(i) for i in range(n))