# https://leetcode.com/problems/jump-game-iii/?envType=daily-question&envId=2026-05-17
# Jump Game III

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)

        q = deque([start])
        visited = [False] * n
        visited[start] = True

        while q:
            i = q.popleft()

            if arr[i] == 0:
                return True

            for ni in (i + arr[i], i - arr[i]):

                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append(ni)

        return False