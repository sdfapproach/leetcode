# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/?envType=daily-question&envId=2024-09-22
# K-th Smallest in Lexicographical Order

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def count_steps(curr, n):
            steps = 0
            first = curr
            last = curr

            while first <= n:
                steps += min(last, n) - first + 1
                first *= 10
                last = last * 10 + 9
            return steps

        current = 1
        k -= 1
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                current += 1
                k -= steps
            else:
                current *= 10
                k -= 1

        return current