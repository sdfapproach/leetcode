# https://leetcode.com/problems/snakes-and-ladders/?envType=daily-question&envId=2025-05-31
# Snakes and Ladders

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        n = len(board)
        target = n * n

        def get_rc(s: int) -> tuple[int, int]:
            idx = s - 1
            row_from_bottom = idx // n
            r = n - 1 - row_from_bottom
            c_in_row = idx % n
            if row_from_bottom % 2 == 0:
                c = c_in_row
            else:
                c = n - 1 - c_in_row
            return r, c

        dist = {}
        dist[1] = 0
        q = deque([1])

        while q:
            s = q.popleft()
            if s == target:
                return dist[s]
            for dice in range(1, 7):
                nxt = s + dice
                if nxt > target:
                    break
                r, c = get_rc(nxt)
                if board[r][c] != -1:
                    nxt = board[r][c]
                if nxt not in dist:
                    dist[nxt] = dist[s] + 1
                    q.append(nxt)

        return -1