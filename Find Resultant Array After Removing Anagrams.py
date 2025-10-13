# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/?envType=daily-question&envId=2025-10-13
# Find Resultant Array After Removing Anagrams

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        ans = []
        prev_sig = None

        for w in words:
            sig = "".join(sorted(w))
            if sig != prev_sig:
                ans.append(w)
                prev_sig = sig

        return ans