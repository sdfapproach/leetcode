# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/submissions/1861669508/?envType=daily-question&envId=2025-12-21
# Delete Columns to Make Sorted II

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])

        deleted = 0
        sorted_pair = [False] * (n - 1)

        for col in range(m):
            bad = False
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                deleted += 1
                continue

            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

        return deleted