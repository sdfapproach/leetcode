# https://leetcode.com/problems/freedom-trail/?envType=daily-question&envId=2024-04-27
# Freedom Trail

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        pos_dict = defaultdict(list)

        for i, ch in enumerate(ring):
            pos_dict[ch].append(i)
        
        n, m = len(ring), len(key)
        dp = [[sys.maxsize] * n for _ in range(m)]
        
        for i in pos_dict[key[0]]:
            dp[0][i] = min(i, n - i) + 1
        
        for i in range(1, m):
            for j in pos_dict[key[i]]:
                for k in pos_dict[key[i-1]]:
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + min(abs(j-k), n-abs(j-k)) + 1)
        
        return min(dp[m-1][j] for j in pos_dict[key[-1]])