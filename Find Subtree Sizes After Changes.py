# https://leetcode.com/problems/find-subtree-sizes-after-changes/?envType=daily-question&envId=2026-11-21
# Find Subtree Sizes After Changes

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        
        n = len(parent)

        graph = [[] for _ in range(n)]

        for i in range(1, n):
            graph[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        stack = [(0, 0, -1)]

        while stack:
            node, state, prev = stack.pop()
            c = s[node]

            if state == 0:
                if c in last:
                    new_parent[node] = last[c]

                old = last.get(c, -1)
                last[c] = node

                stack.append((node, 1, old))

                for child in reversed(graph[node]):
                    stack.append((child, 0, -1))

            else:
                if prev == -1:
                    del last[c]
                else:
                    last[c] = prev

        new_graph = [[] for _ in range(n)]

        for i in range(1, n):
            new_graph[new_parent[i]].append(i)

        answer = [1] * n

        order = [0]

        for node in order:
            for child in new_graph[node]:
                order.append(child)

        for node in reversed(order):
            if node != 0:
                answer[new_parent[node]] += answer[node]

        return answer