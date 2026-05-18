# https://leetcode.com/problems/jump-game-iv/?envType=daily-question&envId=2026-05-18
# Jump Game IV

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)

        if n == 1:
            return 0

        pos = defaultdict(list)

        for i, v in enumerate(arr):
            pos[v].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                next_indices = pos[arr[i]] + [i - 1, i + 1]

                for ni in next_indices:
                    if 0 <= ni < n and not visited[ni]:
                        visited[ni] = True
                        q.append(ni)

                pos[arr[i]].clear()

            steps += 1

        return -1