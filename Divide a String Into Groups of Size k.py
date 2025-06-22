# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/?envType=daily-question&envId=2025-06-22
# Divide a String Into Groups of Size k

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        if len(s) % k != 0:
            s = s + fill * (k - (len(s) % k))

        return [s[i*k : i*k + k] for i in range(math.ceil(len(s) / k))]