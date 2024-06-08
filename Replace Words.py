# https://leetcode.com/problems/replace-words/?envType=daily-question&envId=2024-06-07
# Replace Words

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
    
        words = sentence.split()
        
        def find_shortest_root(word):
            for i in range(1, len(word) + 1):
                if word[:i] in root_set:
                    return word[:i]
            return word
        
        replaced_sentence = ' '.join(find_shortest_root(word) for word in words)
        
        return replaced_sentence