# https://leetcode.com/problems/sum-of-sortable-integers/?envType=daily-question&envId=2026-10-20
# Sum of Sortable Integers

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        
        n = len(nums)
        target = sorted(nums)

        def is_rotation(a, b):
            m = len(a)

            lps = [0] * m
            j = 0

            for i in range(1, m):
                while j > 0 and b[i] != b[j]:
                    j = lps[j - 1]

                if b[i] == b[j]:
                    j += 1
                    lps[i] = j

            j = 0

            for i in range(2 * m - 1):
                x = a[i % m]

                while j > 0 and x != b[j]:
                    j = lps[j - 1]

                if x == b[j]:
                    j += 1

                if j == m:
                    return True

            return False

        answer = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for i in range(0, n, k):
                if not is_rotation(
                    nums[i:i + k],
                    target[i:i + k]
                ):
                    valid = False
                    break

            if valid:
                answer += k

        return answer