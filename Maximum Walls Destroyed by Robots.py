# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/?envType=daily-question&envId=2026-04-03
# Maximum Walls Destroyed by Robots

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        
        if not robots:
            return 0

        U = sorted(list(set(walls)))

        def count(left: int, right: int) -> int:
            if left > right:
                return 0
            return bisect.bisect_right(U, right) - bisect.bisect_left(U, left)

        pos_dict = {}
        for p, d in zip(robots, distance):
            if p not in pos_dict or d > pos_dict[p]:
                pos_dict[p] = d

        sorted_robots = sorted(pos_dict.items())
        n = len(sorted_robots)

        dp = [[0, 0] for _ in range(n)]

        p0, d0 = sorted_robots[0]
        dp[0][0] = count(p0 - d0, p0)
        dp[0][1] = count(p0, p0)

        for i in range(1, n):
            L, d_prev = sorted_robots[i-1]
            R, d_curr = sorted_robots[i]

            wall_at_R = count(R, R)

            X = min(R - 1, L + d_prev)
            Y = max(L + 1, R - d_curr)

            cand1_0 = dp[i-1][0] + count(Y, R - 1) + wall_at_R
            
            if X >= Y:
                cand2_0 = dp[i-1][1] + count(L + 1, R - 1) + wall_at_R
            else:
                cand2_0 = dp[i-1][1] + count(L + 1, X) + count(Y, R - 1) + wall_at_R
                
            dp[i][0] = max(cand1_0, cand2_0)

            cand1_1 = dp[i-1][0] + 0 + wall_at_R
            
            cand2_1 = dp[i-1][1] + count(L + 1, X) + wall_at_R

            dp[i][1] = max(cand1_1, cand2_1)

        p_last, d_last = sorted_robots[-1]
        
        ans = max(dp[n-1][0], dp[n-1][1] + count(p_last + 1, p_last + d_last))

        return ans