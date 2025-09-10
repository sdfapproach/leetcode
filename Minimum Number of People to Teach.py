# https://leetcode.com/problems/minimum-number-of-people-to-teach/?envType=daily-question&envId=2025-09-10
# Minimum Number of People to Teach

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        know = [set()] + [set(langs) for langs in languages]  # pad index 0

        need = set()
        for u, v in friendships:
            if know[u].isdisjoint(know[v]):
                need.add(u); need.add(v)

        if not need:
            return 0

        best = float('inf')
        for ℓ in range(1, n + 1):
            missing = sum(1 for u in need if ℓ not in know[u])
            if missing < best:
                best = missing
        return best