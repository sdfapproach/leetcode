# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/?envType=daily-question&envId=2025-11-05
# Find X-Sum of All K-Long Subarrays II

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def add_to_sets(value: int) -> None:
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            if top_x_set and priority_tuple > top_x_set[0]:
                nonlocal current_sum
                current_sum += priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.add(priority_tuple)
            else:
                remaining_set.add(priority_tuple)
      
        def remove_from_sets(value: int) -> None:
            if frequency_map[value] == 0:
                return
          
            priority_tuple = (frequency_map[value], value)
          
            if priority_tuple in top_x_set:
                nonlocal current_sum
                current_sum -= priority_tuple[0] * priority_tuple[1]  # frequency * value
                top_x_set.remove(priority_tuple)
            else:
                remaining_set.remove(priority_tuple)
      
        top_x_set = SortedList()
        remaining_set = SortedList()
        frequency_map = Counter()
        current_sum = 0
        n = len(nums)
        result = [0] * (n - k + 1)
      
        for i, current_value in enumerate(nums):
            remove_from_sets(current_value)
            frequency_map[current_value] += 1
            add_to_sets(current_value)
          
            window_start = i - k + 1
          
            if window_start < 0:
                continue
          
            while remaining_set and len(top_x_set) < x:
                element = remaining_set.pop()
                top_x_set.add(element)
                current_sum += element[0] * element[1]
          
            while len(top_x_set) > x:
                element = top_x_set.pop(0)
                current_sum -= element[0] * element[1]
                remaining_set.add(element)
          
            result[window_start] = current_sum
          
            leftmost_element = nums[window_start]
            remove_from_sets(leftmost_element)
            frequency_map[leftmost_element] -= 1
            if frequency_map[leftmost_element] > 0:
                add_to_sets(leftmost_element)
      
        return result