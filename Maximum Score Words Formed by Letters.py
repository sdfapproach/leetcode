# https://leetcode.com/problems/maximum-score-words-formed-by-letters/?envType=daily-question&envId=2024-05-24
# Maximum Score Words Formed by Letters

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter

        def word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)

        word_scores = [word_score(word) for word in words]
        
        letter_count = Counter(letters)
        
        max_score = 0
        n = len(words)

        for subset in range(1 << n):
            current_count = letter_count.copy()
            current_score = 0
            valid = True
            
            for i in range(n):
                if subset & (1 << i):
                    word = words[i]
                    for char in word:
                        if current_count[char] < 1:
                            valid = False
                            break
                        current_count[char] -= 1
                    if not valid:
                        break
                    current_score += word_scores[i]
            
            if valid:
                max_score = max(max_score, current_score)
        
        return max_score