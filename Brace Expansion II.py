# https://leetcode.com/problems/brace-expansion-ii/?envType=daily-question&envId=2026-09-25
# Brace Expansion II

class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    next_set, i = parse(i + 1)

                    current = {
                        a + b
                        for a in current
                        for b in next_set
                    }

                    i += 1

                else:
                    ch = expression[i]

                    current = {
                        word + ch
                        for word in current
                    }

                    i += 1

            result |= current

            return result, i

        words, _ = parse(0)

        return sorted(words)