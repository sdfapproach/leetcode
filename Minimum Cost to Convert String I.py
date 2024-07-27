# https://leetcode.com/problems/minimum-cost-to-convert-string-i/?envType=daily-question&envId=2024-07-27
# Minimum Cost to Convert String I

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        if len(source) != len(target):
            return -1

        all_chars = set(source + target + ''.join(original) + ''.join(changed))

        inf = float('inf')
        min_cost = {char: {char2: inf for char2 in all_chars} for char in all_chars}

        for char in all_chars:
            min_cost[char][char] = 0

        for o, c, z in zip(original, changed, cost):
            min_cost[o][c] = min(min_cost[o][c], z)

        for k in all_chars:
            for i in all_chars:
                for j in all_chars:
                    if min_cost[i][j] > min_cost[i][k] + min_cost[k][j]:
                        min_cost[i][j] = min_cost[i][k] + min_cost[k][j]

        total_cost = 0

        for s_char, t_char in zip(source, target):
            if s_char == t_char:
                continue
            if min_cost[s_char][t_char] == inf:
                return -1
            total_cost += min_cost[s_char][t_char]

        return total_cost