# https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/?envType=daily-question&envId=2026-08-28
# Lexicographically Smallest Palindromic Permutation Greater Than Target

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        odd = 0
        mid = ""

        for i in range(26):
            if count[i] % 2:
                odd += 1
                mid = chr(i + ord('a'))

            if odd > 1:
                return ""

        half_count = [c // 2 for c in count]
        h = len(s) // 2
        target_half = target[:h]

        def build_palindrome(left):
            return left + mid + left[::-1]

        remain = half_count[:]
        left = []

        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')

            if remain[idx] == 0:
                possible = False
                break

            remain[idx] -= 1
            left.append(ch)

        if possible:
            candidate = build_palindrome(''.join(left))

            if candidate > target:
                return candidate

        remain = half_count[:]
        prefix = []

        i = 0

        while i < h:
            idx = ord(target_half[i]) - ord('a')

            if remain[idx] == 0:
                break

            remain[idx] -= 1
            prefix.append(target_half[i])
            i += 1

        while True:
            if i < h:
                start = ord(target_half[i]) - ord('a') + 1

                for c in range(start, 26):
                    if remain[c] > 0:
                        ans = prefix + [chr(c + ord('a'))]

                        remain[c] -= 1

                        for x in range(26):
                            if remain[x]:
                                ans.extend(
                                    [chr(x + ord('a'))] * remain[x]
                                )

                        left = ''.join(ans)
                        return build_palindrome(left)

            if i == 0:
                break

            i -= 1

            ch = prefix.pop()
            remain[ord(ch) - ord('a')] += 1

        return ""