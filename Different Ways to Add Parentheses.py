# https://leetcode.com/problems/different-ways-to-add-parentheses/?envType=daily-question&envId=2024-09-19
# Different Ways to Add Parentheses

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        memo = {}
    
        def ways(expression):
            if expression in memo:
                return memo[expression]
            
            res = []
            
            for i, char in enumerate(expression):
                if char in "+-*":
                    left = ways(expression[:i])
                    right = ways(expression[i+1:])
                    
                    for l in left:
                        for r in right:
                            if char == '+':
                                res.append(l + r)
                            elif char == '-':
                                res.append(l - r)
                            elif char == '*':
                                res.append(l * r)
            
            if not res:
                res.append(int(expression))
            
            memo[expression] = res
            return res
        
        return ways(expression)