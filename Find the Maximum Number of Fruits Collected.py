# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/?envType=daily-question&envId=2025-08-07
# Find the Maximum Number of Fruits Collected

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        
        n = len(fruits)
        INF = float('inf')

        first = sum(fruits[i][i] for i in range(n))

        def make_dfs(dirs):
            @lru_cache(None)
            def dfs(r: int, c: int, moves: int) -> int:
                if r == n - 1 and c == n - 1:
                    return 0 if moves == 0 else INF
                if moves == 0 or r == c:
                    return INF

                best = -1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n:
                        val = dfs(nr, nc, moves - 1)
                        if val != INF:
                            best = max(best, val)
                return INF if best < 0 else fruits[r][c] + best
            return dfs

        down_dirs = [(1, -1), (1, 0), (1, 1)]
        dfs_down = make_dfs(down_dirs)
        second = dfs_down(0, n - 1, n - 1)

        right_dirs = [(-1, 1), (0, 1), (1, 1)]
        dfs_right = make_dfs(right_dirs)
        third = dfs_right(n - 1, 0, n - 1)

        return first + second + third