# https://leetcode.com/problems/find-smallest-letter-greater-than-target/?envType=daily-question&envId=2026-01-31
# Find Smallest Letter Greater Than Target

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        greater_targets = [n for n in letters if ord(n) > ord(target)]

        if len(greater_targets) < 1:
            return letters[0]
        else:
            return greater_targets[0]