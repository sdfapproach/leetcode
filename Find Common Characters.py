# https://leetcode.com/problems/find-common-characters/?envType=daily-question&envId=2024-06-05
# Find Common Characters

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common_counter = Counter(words[0])
    
        for word in words[1:]:
            word_counter = Counter(word)
            for char in common_counter:
                if char in word_counter:
                    common_counter[char] = min(common_counter[char], word_counter[char])
                else:
                    common_counter[char] = 0
        
        result = []
        for char, count in common_counter.items():
            result.extend([char] * count)
        
        return result