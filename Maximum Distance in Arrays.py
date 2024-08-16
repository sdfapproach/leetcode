# https://leetcode.com/problems/maximum-distance-in-arrays/?envType=daily-question&envId=2024-08-16
# Maximum Distance in Arrays

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        # max_distance = 0

        # for idx, array in enumerate(arrays):

        #     max_num = max(array)
        #     min_num = min(array)

        #     for arr in arrays[idx+1:]:
                
        #         if abs(min_num - max(arr)) > max_distance:
        #             max_distance = abs(min_num - max(arr))
        #         if abs(max_num - min(arr)) > max_distance:
        #             max_distance = abs(max_num - min(arr))

        # return max_distance

        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            
            current_min = current_array[0]
            current_max = current_array[-1]
            
            max_distance = max(max_distance, abs(current_max - min_val), abs(max_val - current_min))
            
            min_val = min(min_val, current_min)
            max_val = max(max_val, current_max)
        
        return max_distance