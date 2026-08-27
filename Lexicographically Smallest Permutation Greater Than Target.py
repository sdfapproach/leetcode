# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/?envType=daily-question&envId=2026-08-27
# Lexicographically Smallest Permutation Greater Than Target

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        n = len(s)

        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        prefix = []

        i = 0
        while i < n:
            idx = ord(target[i]) - ord('a')

            if count[idx] == 0:
                break

            prefix.append(target[i])
            count[idx] -= 1
            i += 1

        while i >= 0:
            if i < n:
                target_idx = ord(target[i]) - ord('a')

                for c in range(target_idx + 1, 26):
                    if count[c] > 0:
                        answer = prefix + [chr(ord('a') + c)]
                        count[c] -= 1

                        for x in range(26):
                            if count[x]:
                                answer.extend(
                                    [chr(ord('a') + x)] * count[x]
                                )

                        return ''.join(answer)

            if i == 0:
                break

            i -= 1
            ch = prefix.pop()
            count[ord(ch) - ord('a')] += 1

        return ""