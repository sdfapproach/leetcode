# https://leetcode.com/problems/defuse-the-bomb/?envType=daily-question&envId=2024-11-18
# Defuse the Bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0] * len(code)

        elif k >= 1:

            arr = code + code

            for i, num in enumerate(code):

                code[i] = sum(arr[i+1:k+i+1])

            return code

        elif k < 1:

            arr = code[1:] + code

            for i, num in enumerate(code):

                code[i] = sum(arr[i+len(code)+k-1:i+len(code)-1])

            return code