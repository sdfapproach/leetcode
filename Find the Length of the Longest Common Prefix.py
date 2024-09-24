# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/?envType=daily-question&envId=2024-09-24
# Find the Length of the Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        # def common_len(num1, num2):

        #     str1, str2 = str(num1), str(num2)

        #     shorter = min(len(str1), len(str2))

        #     for i in range(shorter):
                
        #         if str1[i] != str2[i]:
        #             return i
            
        #     return shorter

        # length = 0

        # arr1_set, arr2_set = set(arr1), set(arr2)

        # for num1 in arr1_set:
            
        #     for num2 in arr2_set:

        #         length = max(length, common_len(num1, num2))

        # return length


        def get_prefixes(num):
            str_num = str(num)
            prefixes = set()
            for i in range(1, len(str_num) + 1):
                prefixes.add(str_num[:i])
            return prefixes

        prefix_set = set()
        for num1 in arr1:
            prefix_set.update(get_prefixes(num1))
        
        max_length = 0

        for num2 in arr2:
            str_num2 = str(num2)
            for i in range(1, len(str_num2) + 1):
                prefix = str_num2[:i]
                if prefix in prefix_set:
                    max_length = max(max_length, len(prefix))

        return max_length