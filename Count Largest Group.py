# https://leetcode.com/problems/count-largest-group/?envType=daily-question&envId=2025-04-23
# Count Largest Group

class Solution:
    def countLargestGroup(self, n: int) -> int:

        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))
        
        digit_sum_counts = {}
        
        for i in range(1, n + 1):
            digit_sum = sum_of_digits(i)
            if digit_sum not in digit_sum_counts:
                digit_sum_counts[digit_sum] = 0
            digit_sum_counts[digit_sum] += 1
        
        max_size = max(digit_sum_counts.values())
        
        largest_group_count = sum(1 for count in digit_sum_counts.values() if count == max_size)
        
        return largest_group_count