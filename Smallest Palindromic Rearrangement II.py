# https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/?envType=daily-question&envId=2026-07-29
# Smallest Palindromic Rearrangement II

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        
        count = Counter(s)

        middle = ""
        half_count = [0] * 26
        half_length = len(s) // 2

        for ch, frequency in count.items():
            index = ord(ch) - ord('a')
            half_count[index] = frequency // 2

            if frequency % 2 == 1:
                middle = ch

        total = factorial(half_length)

        for frequency in half_count:
            total //= factorial(frequency)

        if total < k:
            return ""

        left = []
        remaining = half_length

        while remaining > 0:
            for index in range(26):
                frequency = half_count[index]

                if frequency == 0:
                    continue

                permutations = total * frequency // remaining

                if k > permutations:
                    k -= permutations
                else:
                    ch = chr(ord('a') + index)
                    left.append(ch)

                    half_count[index] -= 1
                    total = permutations
                    remaining -= 1
                    break

        left = "".join(left)

        return left + middle + left[::-1]