# https://leetcode.com/problems/maximum-score-from-removing-substrings/?envType=daily-question&envId=2024-07-12
# Maximum Score From Removing Substrings

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove_and_score(s, sub1, sub2, points1, points2):
            stack = []
            total_points = 0

            for char in s:
                if stack and stack[-1] + char == sub1:
                    stack.pop()
                    total_points += points1
                else:
                    stack.append(char)
            
            s = ''.join(stack)
            stack = []

            for char in s:
                if stack and stack[-1] + char == sub2:
                    stack.pop()
                    total_points += points2
                else:
                    stack.append(char)
            
            return total_points

        if x >= y:
            return remove_and_score(s, "ab", "ba", x, y)
        else:
            return remove_and_score(s, "ba", "ab", y, x)