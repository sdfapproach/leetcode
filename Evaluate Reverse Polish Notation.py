# https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=daily-question&envId=2024-01-30
# Evaluate Reverse Polish Notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operator = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operator:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                if token == "-":
                    stack.append(a-b)
                if token == "*":
                    stack.append(a*b)
                if token == "/":
                    stack.append(int(a/b))
            else:
                stack.append(int(token))

        return stack.pop()