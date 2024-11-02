# https://leetcode.com/problems/circular-sentence/?envType=daily-question&envId=2024-11-02
# Circular Sentence

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        sentence = sentence.split(" ")
       
        for i, word in enumerate(sentence):

            if i < len(sentence)-1:
                if word[-1] != sentence[i+1][0]:
                    return False

            else:
                if word[-1] != sentence[0][0]:
                    return False

        return True