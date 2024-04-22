# https://leetcode.com/problems/open-the-lock/?envType=daily-question&envId=2024-04-22
# Open the Lock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

        dead = set(deadends)
        queue = deque([('0000', 0)])
        seen = {'0000'}

        if '0000' in dead:
            return -1

        while queue:
            node, depth = queue.popleft()
            if node == target:
                return depth
            for neighbor in neighbors(node):
                if neighbor not in seen and neighbor not in dead:
                    seen.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return -1