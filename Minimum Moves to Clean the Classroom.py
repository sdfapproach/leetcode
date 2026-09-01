# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/?envType=daily-question&envId=2026-09-01
# Minimum Moves to Clean the Classroom

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        m = len(classroom)
        n = len(classroom[0])

        start = None
        litter = {}
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = litter_count
                    litter_count += 1

        target_mask = (1 << litter_count) - 1

        if target_mask == 0:
            return 0

        sr, sc = start

        best = [
            [
                [-1] * (1 << litter_count)
                for _ in range(n)
            ]
            for _ in range(m)
        ]

        best[sr][sc][0] = energy

        queue = deque([
            (sr, sc, 0, energy, 0)
        ])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c, mask, remain, moves = queue.popleft()

            if mask == target_mask:
                return moves

            if remain == 0:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                new_energy = remain - 1
                new_mask = mask

                if classroom[nr][nc] == 'L':
                    bit = litter[(nr, nc)]
                    new_mask |= 1 << bit

                if classroom[nr][nc] == 'R':
                    new_energy = energy

                if new_mask == target_mask:
                    return moves + 1

                if best[nr][nc][new_mask] >= new_energy:
                    continue

                best[nr][nc][new_mask] = new_energy

                queue.append(
                    (
                        nr,
                        nc,
                        new_mask,
                        new_energy,
                        moves + 1
                    )
                )

        return -1