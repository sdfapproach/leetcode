# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/?envType=daily-question&envId=2026-07-19
# Smallest Subsequence of Distinct Characters

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        last_index = {}

        for i, ch in enumerate(s):
            last_index[ch] = i

        stack = []
        used = set()

        for i, ch in enumerate(s):
            if ch in used:
                continue

            while (
                stack
                and stack[-1] > ch
                and last_index[stack[-1]] > i
            ):
                removed = stack.pop()
                used.remove(removed)

            stack.append(ch)
            used.add(ch)

        return ''.join(stack)