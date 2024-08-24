# https://leetcode.com/problems/find-the-closest-palindrome/?envType=daily-question&envId=2024-08-24
# Find the Closest Palindrome

class Solution:
    def nearestPalindromic(self, n: str) -> str:

        if len(n) == 1:
            return str(int(n) - 1)
        
        num = int(n)
        length = len(n)
        
        candidates = [
            10**(length - 1) - 1,
            10**length + 1
        ]
        
        prefix = int(n[:(length + 1) // 2])
        
        for i in range(prefix - 1, prefix + 2):
            candidate = str(i)
            if length % 2 == 0:
                candidate += candidate[::-1]
            else:
                candidate += candidate[-2::-1]
            candidates.append(int(candidate))
        
        candidates = [c for c in candidates if c != num]

        return str(min(candidates, key=lambda x: (abs(x - num), x)))