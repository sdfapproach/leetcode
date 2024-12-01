# https://leetcode.com/problems/check-if-n-and-its-double-exist/?envType=daily-question&envId=2024-12-01
# Check If N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        for i, num in enumerate(arr):

            for j in range(len(arr)):

                if i == j:
                    continue
                    
                if arr[j] * 2 == num:
                    return True

        return False