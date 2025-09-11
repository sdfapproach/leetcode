# https://leetcode.com/problems/sort-vowels-in-a-string/?envType=daily-question&envId=2025-09-11
# Sort Vowels in a String

class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = set("aeiouAEIOU")
        idxs = [i for i, ch in enumerate(s) if ch in vowels]
        arr = list(s)
        vs = sorted(arr[i] for i in idxs)  # ASCII ascending
        for i, ch in zip(idxs, vs):
            arr[i] = ch
        return "".join(arr)