# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/?envType=daily-question&envId=2026-08-14
# Maximum Length Substring With Two Occurrences

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        count = defaultdict(int)

        left = 0
        answer = 0

        for right, ch in enumerate(s):
            count[ch] += 1

            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer