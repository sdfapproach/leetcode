# https://leetcode.com/problems/count-the-number-of-consistent-strings/?envType=daily-question&envId=2024-09-12
# Count the Number of Consistent Strings

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        word_set = set(allowed)

        def check(s) -> bool:

            for char in set(s):

                if char not in word_set:
                    return False

            return True

        count = 0
        
        for word in words:

            if check(word) == True:
                count += 1

        return count