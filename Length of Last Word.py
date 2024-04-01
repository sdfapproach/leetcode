# https://leetcode.com/problems/length-of-last-word/?envType=daily-question&envId=2024-04-01
# Length of Last Word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # s = s.strip()

        # count = 0

        # for char in s:
        #     if char == " ":
        #         count = 0
        #     else:
        #         count += 1

        # return count

        return len(s.strip().split()[-1])