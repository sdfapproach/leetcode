# https://leetcode.com/problems/maximum-building-height/?envType=daily-question&envId=2026-06-20
# Maximum Building Height

class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        
        restrictions.append([1, 0])
        restrictions.sort()

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        for i in range(1, len(restrictions)):
            prev_id, prev_h = restrictions[i - 1]
            cur_id, cur_h = restrictions[i]

            restrictions[i][1] = min(cur_h, prev_h + cur_id - prev_id)

        for i in range(len(restrictions) - 2, -1, -1):
            next_id, next_h = restrictions[i + 1]
            cur_id, cur_h = restrictions[i]

            restrictions[i][1] = min(cur_h, next_h + next_id - cur_id)

        ans = 0

        for i in range(1, len(restrictions)):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]

            dist = id2 - id1

            peak = (h1 + h2 + dist) // 2
            ans = max(ans, peak)

        return ans