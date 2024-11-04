# https://leetcode.com/problems/string-compression-iii/?envType=daily-question&envId=2024-11-04
# String Compression III

class Solution:
    def compressedString(self, word: str) -> str:
        
        comp = ""
        count = 1
        current = word[0]

        for i in range(1, len(word)):

            if current == word[i]:
                
                if count == 9:
                    comp += "9"
                    comp += current
                    count -= 8
                else:
                    count += 1

            else:
                comp += str(count)
                comp += current

                current = word[i]
                count = 1
        
        comp += str(count)
        comp += current

        # count_word = Counter(word)
        
        # while count_word:
        #     # max_key, max_value = max(count_word.items(), key=lambda x: x[1])
        #     most_common = count_word.most_common()
        #     max_key, max_value = most_common[0][0], most_common[0][1]

        #     if max_value > 9:
        #         comp += "9" + max_key
        #         count_word[max_key] -= 9

        #         if max_value < 1:
        #             del count_word[max_key]
        #         else:
        #             count_word[max_key] = max_value - 9

        #     else:
        #         comp += str(max_value) + max_key
        #         del count_word[max_key]
            
        return comp