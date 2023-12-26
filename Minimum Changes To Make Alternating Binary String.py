# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/?envType=daily-question&envId=2023-12-24
# Minimum Changes To Make Alternating Binary String

class Solution:
    def minOperations(self, s: str) -> int:
        # change1 = 0
        # change2 = 0

        # str1 = ""
        # for i in range(len(s)):
        #     if i%2==0:
        #         str1 += "1"
        #     else:
        #         str1 += "0"

        # str2 = ""
        # for i in range(len(s)):
        #     if i%2==1:
        #         str2 += "1"
        #     else:
        #         str2 += "0"
        
        # for i in range(len(s)):
        #     if str1[i] != s[i]:
        #         change1 += 1

        # for i in range(len(s)):
        #     if str2[i] != s[i]:
        #         change2 += 1
        
        # if change1 <= change2:
        #     return change1
        # else:
        #     return change2

        count_changes1 = sum(1 for i, c in enumerate(s) if i % 2 == int(c))
        count_changes2 = sum(1 for i, c in enumerate(s) if i % 2 != int(c))

        return min(count_changes1, count_changes2)