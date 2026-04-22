# https://leetcode.com/problems/words-within-two-edits-of-dictionary/?envType=daily-question&envId=2026-04-22
# Words Within Two Edits of Dictionary

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        res = []
        
        for q in queries:
            for d in dictionary:
                diff = 0
                
                for a, b in zip(q, d):
                    if a != b:
                        diff += 1
                        if diff > 2:
                            break
                
                if diff <= 2:
                    res.append(q)
                    break
        
        return res