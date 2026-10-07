# https://leetcode.com/problems/remove-invalid-parentheses/?envType=daily-question&envId=2026-10-07
# Remove Invalid Parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}

        while queue:
            answer = []

            for _ in range(len(queue)):
                current = queue.popleft()

                if is_valid(current):
                    answer.append(current)

                for i, ch in enumerate(current):

                    if ch not in '()':
                        continue

                    next_string = current[:i] + current[i + 1:]

                    if next_string not in visited:
                        visited.add(next_string)
                        queue.append(next_string)

            if answer:
                return answer

        return [""]