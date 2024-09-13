# https://leetcode.com/problems/xor-queries-of-a-subarray/?envType=daily-question&envId=2024-09-13
# XOR Queries of a Subarray

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        # sub_array = []

        # for querie in queries:

        #     xor = arr[querie[0]]

        #     if len(arr[querie[0]:querie[1]]) > 0:

        #         for num in arr[querie[0]+1:querie[1]+1]:
        #             xor ^= num

        #     sub_array.append(xor)

        # return sub_array

        prefix = [0]

        for num in arr:
            prefix.append(prefix[-1] ^ num)
        
        result = []

        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])

        return result