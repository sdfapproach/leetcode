# https://leetcode.com/problems/sequential-digits/?envType=daily-question&envId=2024-02-02
# Sequential Digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # nums = []
        
        # for i in range(1, len(str(high))):
        #     for j in range(1, 10-i):
        #         num = str(j)
        #         for k in range(i):
        #             num += str((j+1)+k)
        #         nums.append(int(num))

        # return [num for num in nums if num >= low and num <= high]

        seq_digits = "123456789"
        result = []

        for length in range(len(str(low)), len(str(high)) + 1):
            for start in range(10 - length):
                num = int(seq_digits[start:start + length])
                if low <= num <= high:
                    result.append(num)

        return result