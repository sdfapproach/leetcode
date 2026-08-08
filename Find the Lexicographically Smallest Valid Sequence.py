# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/?envType=daily-question&envId=2026-08-08
# Find the Lexicographically Smallest Valid Sequence

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        
        n, m = len(word1), len(word2)

        if m > n:
            return []

        suffix = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                j -= 1

            suffix[i] = m - 1 - j

        ans = []
        target_idx = 0
        mismatch_used = False

        for i in range(n):
            if target_idx == m:
                break

            if word1[i] == word2[target_idx]:
                ans.append(i)
                target_idx += 1

            elif not mismatch_used:
                remaining = m - target_idx - 1

                if suffix[i + 1] >= remaining:
                    ans.append(i)
                    target_idx += 1
                    mismatch_used = True

        return ans if target_idx == m else []