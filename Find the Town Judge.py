# https://leetcode.com/problems/find-the-town-judge/?envType=daily-question&envId=2024-02-22
# Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # people = set([n[0] for n in trust])

        # judges = set([n[1] for n in trust])

        # candidates = [judge for judge in judges if judge not in people]

        # if len(candidates) <= 0:
        #     return -1

        # print(candidates)

        if n == 1 and not trust:
            return 1

        trust_counts = [0] * (n + 1)
        trusted_by = [0] * (n + 1)

        for a, b in trust:
            trust_counts[b] += 1
            trusted_by[a] += 1

        for i in range(1, n + 1):
            if trust_counts[i] == n - 1 and trusted_by[i] == 0:
                return i

        return -1