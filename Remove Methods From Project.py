# https://leetcode.com/problems/remove-methods-from-project/?envType=daily-question&envId=2026-08-05
# Remove Methods From Project

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        suspicious = set()
        stack = [k]

        while stack:
            method = stack.pop()

            if method in suspicious:
                continue

            suspicious.add(method)

            for nxt in graph[method]:
                stack.append(nxt)

        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        return [
            method
            for method in range(n)
            if method not in suspicious
        ]