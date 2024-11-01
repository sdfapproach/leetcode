# https://leetcode.com/problems/delete-characters-to-make-fancy-string/?envType=daily-question&envId=2024-11-01
# Delete Characters to Make Fancy String

class Solution:
    def makeFancyString(self, s: str) -> str:
        
        char = ""
        count = 1
        fancy_string = ""

        for c in s:

            if c == char:
                
                count += 1

                if count < 3:
                    fancy_string += c

            else:
                count = 1
                char = c
                fancy_string += c

        return fancy_string