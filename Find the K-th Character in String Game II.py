# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/?envType=daily-question&envId=2025-07-04
# Find the K-th Character in String Game II

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        # word = "a"

        # for op in operations:
        #     if op == 0:
        #         word += word
        #     else:

        #         string = ""

        #         for c in word:

        #             string += chr((ord(c) % 122) + 1)

        #         word += string

        # return word[k-1]

        m = len(operations)
        lengths = [0]*(m+1)
        lengths[0] = 1
        for i, op in enumerate(operations, start=1):
            lengths[i] = min(lengths[i-1]*2, k)
        
        def find_char(op_idx: int, pos: int) -> str:
            if op_idx == 0:
                return 'a'
            
            prev_len = lengths[op_idx-1]
            op = operations[op_idx-1]
            
            if pos <= prev_len:
                return find_char(op_idx-1, pos)
            else:
                pos -= prev_len
                if op == 0:
                    return find_char(op_idx-1, pos)
                else:
                    orig = find_char(op_idx-1, pos)
                    return chr((ord(orig) - ord('a') + 1) % 26 + ord('a'))
        
        return find_char(m, k)