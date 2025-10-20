# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/?envType=daily-question&envId=2025-10-20
# Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0

        for operation in operations:
            if operation == "--X":
                x -= 1
            elif operation == "X--":
                x -= 1
            elif operation == "++X":
                x += 1
            elif operation == "X++":
                x += 1

        return x