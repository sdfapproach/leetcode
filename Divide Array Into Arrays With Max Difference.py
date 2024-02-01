# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/?envType=daily-question&envId=2024-02-01
# Divide Array Into Arrays With Max Difference

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # arr =[]
        
        # nums.sort()

        # sub_arr = []

        # for i, num in enumerate(nums):
        #     sub_arr.append(num)
        #     if (i+1)%3==0:
        #         arr.append(sub_arr)
        #         sub_arr = []

        # for a in arr:
        #     if abs(a[0]-a[1])>k:
        #         return []
        #     if abs(a[0]-a[2])>k:
        #         return []
        #     if abs(a[1]-a[2])>k:
        #         return []

        # return arr

        nums.sort()
        arr = []

        for i in range(0, len(nums), 3):
            if i + 2 < len(nums):
                sub_arr = [nums[i], nums[i + 1], nums[i + 2]]
                if abs(sub_arr[1] - sub_arr[0]) > k or abs(sub_arr[2] - sub_arr[1]) > k:
                    return []
                arr.append(sub_arr)
            else:
                break

        return arr