# https://leetcode.com/problems/find-if-array-can-be-sorted/?envType=daily-question&envId=2024-11-06
# Find if Array Can Be Sorted

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        def one_counter(num):
            count = 0
            for n in bin(num)[2:]:
                if n == '1':
                    count += 1
            return count

        sorting = True

        while sorting:

            sorting = False

            for i in range(1, len(nums)):

                if nums[i] < nums[i-1]:

                    if one_counter(nums[i]) == one_counter(nums[i-1]):
                        temp = nums[i]
                        nums[i] = nums[i-1]
                        nums[i-1] = temp

                        sorting = True
                    else:
                        return False

        # i = 1

        # while i < len(nums):

        #     if nums[i] < nums[i-1]:

        #         if one_counter(nums[i]) == one_counter(nums[i-1]):
        #             temp = nums[i]
        #             nums[i] = nums[i-1]
        #             nums[i-1] = temp

        #             i = 1
        #         else:
        #             return False
        #     else:
        #         i += 1

        # def one_counter(num):
        #     return bin(num).count('1')
        
        # groups = defaultdict(list)
        # for num in nums:
        #     groups[one_counter(num)].append(num)
        
        # for key in groups:
        #     groups[key].sort()
        
        # index = 0
        # for key in sorted(groups.keys()):
        #     for num in groups[key]:
        #         if nums[index] != num:
        #             return False
        #         index += 1

        return True