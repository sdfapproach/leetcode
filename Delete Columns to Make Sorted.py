# https://leetcode.com/problems/delete-columns-to-make-sorted/?envType=daily-question&envId=2025-12-20
# Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        ans = 0

        for col in range(m):
            for row in range(n - 1):
                if strs[row][col] > strs[row + 1][col]:
                    ans += 1
                    break
        return ans