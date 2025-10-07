# https://leetcode.com/problems/avoid-flood-in-the-city/?envType=daily-question&envId=2025-10-07
# Avoid Flood in The City

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        n = len(rains)
        ans = [1] * n
        last = {}
        dryDays = []

        for i, lake in enumerate(rains):
            if lake == 0:
                dryDays.append(i)
            else:
                ans[i] = -1
                if lake in last:
                    j = last[lake]
                    k = bisect_right(dryDays, j)
                    if k == len(dryDays):
                        return []
                    d = dryDays.pop(k)
                    ans[d] = lake
                last[lake] = i

        return ans