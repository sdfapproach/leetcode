# https://leetcode.com/problems/move-pieces-to-obtain-a-string/?envType=daily-question&envId=2024-12-05
# Move Pieces to Obtain a String

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        start_positions = [(i, c) for i, c in enumerate(start) if c != '_']
        target_positions = [(i, c) for i, c in enumerate(target) if c != '_']

        if len(start_positions) != len(target_positions):
            return False

        for (start_idx, start_char), (target_idx, target_char) in zip(start_positions, target_positions):
            if start_char != target_char:
                return False
            if start_char == 'L' and start_idx < target_idx:
                return False
            if start_char == 'R' and start_idx > target_idx:
                return False

        return True