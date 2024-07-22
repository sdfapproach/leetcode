# https://leetcode.com/problems/sort-the-people/?envType=daily-question&envId=2024-07-22
# Sort the People

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # heights = [[idx, height] for idx, height in enumerate(heights)]

        # heights.sort(key = lambda x : x[1], reverse=True)

        # return [names[i[0]] for i in heights]

        combined = zip(names, heights)
    
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)

        return [name for name, height in sorted_combined]