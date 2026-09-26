# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/?envType=daily-question&envId=2026-09-26
# Evaluate the Bracket Pairs of a String

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        knowledge = dict(knowledge)

        answer = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                j = i + 1

                while s[j] != ')':
                    j += 1

                key = s[i + 1:j]

                answer.append(
                    knowledge.get(key, "?")
                )

                i = j + 1

            else:
                answer.append(s[i])
                i += 1

        return ''.join(answer)