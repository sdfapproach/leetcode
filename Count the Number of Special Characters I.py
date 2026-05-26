# https://leetcode.com/problems/count-the-number-of-special-characters-i/?envType=daily-question&envId=2026-05-26
# Count the Number of Special Characters I

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        return list(Counter("".join(list(set(word))).lower()).values()).count(2)

        # count = 0
        
        # for value in Counter("".join(list(set(word))).lower()).values():
            
        #     if value == 2:
        #         count += 1

        # return count