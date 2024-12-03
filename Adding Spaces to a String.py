# https://leetcode.com/problems/adding-spaces-to-a-string/?envType=daily-question&envId=2024-12-03
# Adding Spaces to a String

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        # count = 0

        # s_list = list(s)

        # for n in spaces:
        #     s_list.insert(count+n, " ")
        #     count += 1

        # return "".join(s_list)

        idx = 0

        text = ""

        for i, n in enumerate(spaces):

            text += s[idx:n]
            text += " "
            idx = n

        text += s[idx:]

        return text