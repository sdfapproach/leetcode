# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/?envType=daily-question&envId=2026-09-18
# Maximum Number of Non-Overlapping Substrings

class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]
            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                if first[x] < left:
                    valid = False
                    break

                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        intervals.sort(key=lambda x: x[1])

        answer = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                answer.append(s[left:right + 1])
                prev_end = right

        return answer