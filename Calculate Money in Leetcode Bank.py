# https://leetcode.com/problems/calculate-money-in-leetcode-bank/?envType=daily-question&envId=2025-10-25
# Calculate Money in Leetcode Bank

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        full_weeks = n // 7
        extra_days = n % 7

        full_weeks_sum = (
            7 * (full_weeks - 1) * full_weeks // 2
            + 28 * full_weeks
        )

        extra_sum = (
            extra_days * (1 + full_weeks)
            + (extra_days - 1) * extra_days // 2
        )

        return full_weeks_sum + extra_sum