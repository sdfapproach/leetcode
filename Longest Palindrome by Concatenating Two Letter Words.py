# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/?envType=daily-question&envId=2025-05-25
# Longest Palindrome by Concatenating Two Letter Words

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        count = Counter(words)
        palindrome_length = 0
        center_used = False

        for word, freq in count.items():
            reversed_word = word[::-1]

            if word == reversed_word:
                palindrome_length += (freq // 2) * 4
                if freq % 2 == 1:
                    center_used = True
            elif reversed_word in count:
                if word < reversed_word:
                    pairs = min(freq, count[reversed_word])
                    palindrome_length += pairs * 4

        if center_used:
            palindrome_length += 2

        return palindrome_length
