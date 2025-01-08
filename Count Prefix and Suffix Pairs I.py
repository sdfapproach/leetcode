# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/?envType=daily-question&envId=2025-01-08
# Count Prefix and Suffix Pairs I

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def isPrefixAndSuffix(str1, str2):

            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        
        for i, word in enumerate(words):

            for str2 in words[i+1:]:
                if isPrefixAndSuffix(word, str2):
                    count += 1

        return count