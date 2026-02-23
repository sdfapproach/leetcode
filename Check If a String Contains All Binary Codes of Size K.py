# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/?envType=daily-question&envId=2026-02-23
# Check If a String Contains All Binary Codes of Size K

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        n = len(s)
        
        if k > n:
            return False
        
        need = 1 << k
        
        if n - k + 1 < need:
            return False
        
        seen = [False] * need
        mask = need - 1
        
        val = 0
        count = 0
        
        for i in range(n):
            val = ((val << 1) & mask) | int(s[i])
            
            if i >= k - 1:
                if not seen[val]:
                    seen[val] = True
                    count += 1
                    
                    if count == need:
                        return True
        
        return False