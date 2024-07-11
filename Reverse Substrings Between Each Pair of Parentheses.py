# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/?envType=daily-question&envId=2024-07-11
# Reverse Substrings Between Each Pair of Parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []

        for char in s:

            if char == ")":

                sub_string = []

                while len(stack) > 0:
                    
                    if stack[-1] == "(":
                        stack.pop()
                        break

                    sub_string.append(stack.pop())

                stack.extend(sub_string)

            else:
                stack.append(char)

        return "".join(stack)