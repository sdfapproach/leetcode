# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/?envType=daily-question&envId=2024-10-19
# Find Kth Bit in Nth Binary String

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        s = ["0", "011"]

        for i in range(2, n):
            s.append(s[i-1] + "1" + "".join("1" if c == "0" else "0" for c in s[i-1][::-1]))

        return s[n-1][k-1]