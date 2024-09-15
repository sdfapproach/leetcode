# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/?envType=daily-question&envId=2024-09-15
# Find the Longest Substring Containing Vowels in Even Counts

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowel_to_bit = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        state_to_index = {0: -1}
        state = 0
        max_length = 0

        for index, char in enumerate(s):
            if char in vowel_to_bit:
                state ^= vowel_to_bit[char]

            if state in state_to_index:
                max_length = max(max_length, index - state_to_index[state])
            else:
                state_to_index[state] = index

        return max_length