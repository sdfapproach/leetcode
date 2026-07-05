# https://leetcode.com/problems/number-of-paths-with-max-score/?envType=daily-question&envId=2026-07-05
# Number of Paths with Max Score

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
        MOD = 10**9 + 7
        n = len(board)

        dp_score = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]

        dp_score[n - 1][n - 1] = 0
        dp_count[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X':
                    continue

                if dp_count[i][j] == 0:
                    continue

                for ni, nj in [(i - 1, j), (i, j - 1), (i - 1, j - 1)]:
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != 'X':
                        val = 0
                        if board[ni][nj].isdigit():
                            val = int(board[ni][nj])

                        new_score = dp_score[i][j] + val

                        if new_score > dp_score[ni][nj]:
                            dp_score[ni][nj] = new_score
                            dp_count[ni][nj] = dp_count[i][j]

                        elif new_score == dp_score[ni][nj]:
                            dp_count[ni][nj] = (dp_count[ni][nj] + dp_count[i][j]) % MOD

        if dp_count[0][0] == 0:
            return [0, 0]

        return [dp_score[0][0], dp_count[0][0] % MOD]