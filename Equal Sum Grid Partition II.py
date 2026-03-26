# https://leetcode.com/problems/equal-sum-grid-partition-ii/?envType=daily-question&envId=2026-03-26
# Equal Sum Grid Partition II

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        m = len(grid)
        n = len(grid[0])

        val_stats = {}
        total_sum = 0
        row_sums = [0] * m
        col_sums = [0] * n

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                total_sum += val
                row_sums[r] += val
                col_sums[c] += val

                if val not in val_stats:
                    val_stats[val] = {'min_r': r, 'max_r': r, 'min_c': c, 'max_c': c}
                else:
                    val_stats[val]['min_r'] = min(val_stats[val]['min_r'], r)
                    val_stats[val]['max_r'] = max(val_stats[val]['max_r'], r)
                    val_stats[val]['min_c'] = min(val_stats[val]['min_c'], c)
                    val_stats[val]['max_c'] = max(val_stats[val]['max_c'], c)

        def can_discount_top(val, i):
            if val not in val_stats: return False
            R, C = i + 1, n
            if R >= 2 and C >= 2: return val_stats[val]['min_r'] <= i
            if R == 1: return grid[0][0] == val or grid[0][n-1] == val
            if C == 1: return grid[0][0] == val or grid[i][0] == val
            return False

        def can_discount_bot(val, i):
            if val not in val_stats: return False
            R, C = m - 1 - i, n
            if R >= 2 and C >= 2: return val_stats[val]['max_r'] >= i + 1
            if R == 1: return grid[m-1][0] == val or grid[m-1][n-1] == val
            if C == 1: return grid[i+1][0] == val or grid[m-1][0] == val
            return False

        def can_discount_left(val, j):
            if val not in val_stats: return False
            R, C = m, j + 1
            if R >= 2 and C >= 2: return val_stats[val]['min_c'] <= j
            if R == 1: return grid[0][0] == val or grid[0][j] == val
            if C == 1: return grid[0][0] == val or grid[m-1][0] == val
            return False

        def can_discount_right(val, j):
            if val not in val_stats: return False
            R, C = m, n - 1 - j
            if R >= 2 and C >= 2: return val_stats[val]['max_c'] >= j + 1
            if R == 1: return grid[0][j+1] == val or grid[0][n-1] == val
            if C == 1: return grid[0][n-1] == val or grid[m-1][n-1] == val
            return False

        current_top_sum = 0
        for i in range(m - 1):
            current_top_sum += row_sums[i]
            top_sum = current_top_sum
            bot_sum = total_sum - top_sum

            if top_sum == bot_sum: return True
            diff = abs(top_sum - bot_sum)

            if top_sum > bot_sum and can_discount_top(diff, i): return True
            if bot_sum > top_sum and can_discount_bot(diff, i): return True

        current_left_sum = 0
        for j in range(n - 1):
            current_left_sum += col_sums[j]
            left_sum = current_left_sum
            right_sum = total_sum - left_sum

            if left_sum == right_sum: return True
            diff = abs(left_sum - right_sum)

            if left_sum > right_sum and can_discount_left(diff, j): return True
            if right_sum > left_sum and can_discount_right(diff, j): return True

        return False