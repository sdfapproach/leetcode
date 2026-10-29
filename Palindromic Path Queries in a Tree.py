# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/?envType=daily-question&envId=2026-10-29
# Palindromic Path Queries in a Tree

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        size = [1] * n
        heavy = [-1] * n

        order = [0]

        for u in order:
            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        for u in reversed(order):
            max_size = 0

            for v in graph[u]:
                if v == parent[u]:
                    continue

                size[u] += size[v]

                if size[v] > max_size:
                    max_size = size[v]
                    heavy[u] = v

        head = [0] * n
        pos = [0] * n
        current = 0

        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = current
                current += 1

                for v in graph[u]:
                    if v != parent[u] and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        size_tree = 1

        while size_tree < n:
            size_tree *= 2

        tree = [0] * (2 * size_tree)

        chars = list(s)

        for u in range(n):
            mask = 1 << (ord(chars[u]) - ord('a'))
            tree[size_tree + pos[u]] = mask

        for i in range(size_tree - 1, 0, -1):
            tree[i] = tree[i * 2] ^ tree[i * 2 + 1]

        def update(u, c):
            i = size_tree + pos[u]
            tree[i] = 1 << (ord(c) - ord('a'))

            i //= 2

            while i:
                tree[i] = tree[i * 2] ^ tree[i * 2 + 1]
                i //= 2

        def range_query(left, right):
            left += size_tree
            right += size_tree

            result = 0

            while left <= right:
                if left % 2 == 1:
                    result ^= tree[left]
                    left += 1

                if right % 2 == 0:
                    result ^= tree[right]
                    right -= 1

                left //= 2
                right //= 2

            return result

        def path_query(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_query(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_query(pos[u], pos[v])

            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]

                update(u, c)

            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_query(u, v)

                answer.append(
                    mask & (mask - 1) == 0
                )

        return answer