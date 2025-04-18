# https://leetcode.com/problems/count-and-say/?envType=daily-question&envId=2025-04-18
# Count and Say

class Solution:
    def countAndSay(self, n: int) -> str:
        
        result = "1"
    
        for _ in range(1, n):
            next_result = []
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                next_result.append(str(count) + result[i])
                i += 1
            
            result = ''.join(next_result)
        
        return result