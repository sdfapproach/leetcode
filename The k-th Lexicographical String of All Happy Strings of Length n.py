# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/?envType=daily-question&envId=2025-02-19
# The k-th Lexicographical String of All Happy Strings of Length n

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        happy_strings = []
        
        def backtrack(path: str):
            if len(path) == n:
                happy_strings.append(path)
                return
            for ch in "abc":
                if not path or path[-1] != ch:
                    backtrack(path + ch)
        
        backtrack("")
        
        happy_strings.sort()
        
        return happy_strings[k - 1] if k <= len(happy_strings) else ""