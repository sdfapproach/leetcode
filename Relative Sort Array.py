# https://leetcode.com/problems/relative-sort-array/?envType=daily-question&envId=2024-06-11
# Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # count = Counter(arr1)

        # arr = []

        # for num in arr2:

        #     for _ in range(count[num]):
        #         arr.append(num)
            
        #     del count[num]

        # count_list = []

        # for key, val in count.items():
        #     count_list.extend([key] * val)

        # count_list.sort()

        # return arr + count_list

        count = Counter(arr1)
        result = []
        
        for num in arr2:
            result.extend([num] * count.pop(num))
        
        remaining_elements = sorted(count.elements())
        result.extend(remaining_elements)
        
        return result