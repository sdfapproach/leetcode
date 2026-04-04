# https://leetcode.com/problems/decode-the-slanted-ciphertext/?envType=daily-question&envId=2026-04-04
# Decode the Slanted Ciphertext

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        
        if not encodedText:
            return ""
        
        cols = len(encodedText) // rows
        
        matrix = [
            list(encodedText[i * cols:(i + 1) * cols])
            for i in range(rows)
        ]
        
        res = []
        
        for start_col in range(cols):
            i, j = 0, start_col
            
            while i < rows and j < cols:
                res.append(matrix[i][j])
                i += 1
                j += 1
        
        return "".join(res).rstrip()