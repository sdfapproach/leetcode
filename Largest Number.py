# https://leetcode.com/problems/largest-number/?envType=daily-question&envId=2024-09-18
# Largest Number

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # strs = [str(num) for num in nums]

        # return str(int("".join(sorted(strs, key=lambda x : (str(x) * 10)[:100], reverse=True))))

        strs = [str(num) for num in nums]
    
        strs.sort(key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1))
        
        return str(int("".join(strs)))