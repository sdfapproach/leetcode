# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/?envType=daily-question&envId=2024-09-02
# Find the Student that Will Replace the Chalk

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        total_chalk = sum(chalk)
        k = k % total_chalk

        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]