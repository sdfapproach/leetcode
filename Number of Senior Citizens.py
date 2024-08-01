# https://leetcode.com/problems/number-of-senior-citizens/?envType=daily-question&envId=2024-08-01
# Number of Senior Citizens

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0

        for string in details:
            if int(string[11:13]) > 60:
                count += 1

        return count