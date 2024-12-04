# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/?envType=daily-question&envId=2024-12-04
# Make String a Subsequence Using Cyclic Increments

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        idx = 0

        for char_2 in str2:

            flag = False

            for i, char_1 in enumerate(str1[idx:]):

                if char_2 == char_1:
                    idx += (i+1)
                    flag = True
                    break
                elif char_1 != 'z' and char_2 == chr(ord(char_1) + 1):
                    idx += (i+1)
                    flag = True
                    break
                elif char_1 == 'z' and char_2 == 'a':
                    idx += (i+1)
                    flag = True
                    break
            
            if flag == False:
                return False

        return True