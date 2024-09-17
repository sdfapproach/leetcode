# https://leetcode.com/problems/uncommon-words-from-two-sentences/?envType=daily-question&envId=2024-09-17
# Uncommon Words from Two Sentences

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        token_s1 = s1.split(" ")
        token_s2 = s2.split(" ")

        return [word[0] for word in (Counter(token_s1) + Counter(token_s2)).items() if word[1] == 1]