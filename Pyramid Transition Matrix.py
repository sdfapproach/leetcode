# https://leetcode.com/problems/pyramid-transition-matrix/?envType=daily-question&envId=2025-12-29
# Pyramid Transition Matrix

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        trans = defaultdict(set)

        for a, b, c in allowed:
            trans[(a, b)].add(c)

        memo = set()

        def dfs(curr: str) -> bool:
            if len(curr) == 1:
                return True

            if curr in memo:
                return False

            candidates = []

            def build(idx: int, path: str):
                if idx == len(curr) - 1:
                    candidates.append(path)
                    return

                pair = (curr[idx], curr[idx + 1])
                if pair not in trans:
                    return

                for ch in trans[pair]:
                    build(idx + 1, path + ch)

            build(0, "")

            for nxt in candidates:
                if dfs(nxt):
                    return True

            memo.add(curr)
            return False

        return dfs(bottom)