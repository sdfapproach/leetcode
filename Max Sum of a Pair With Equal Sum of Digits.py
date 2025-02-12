# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/?envType=daily-question&envId=2025-02-12
# Max Sum of a Pair With Equal Sum of Digits

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        # def sum_digit(num):

        #     number = 0
            
        #     for n in str(num):
        #         number += int(n)

        #     return number
        
        # dics = []

        # max_num = 0

        # for i, num in enumerate(nums):

        #     dics.append([i,sum_digit(num)])

        # sum_list = []

        # for i, dic in enumerate(dics):

        #     for j in range(i+1, len(dics)):
                
        #         if dic[1] == dics[j][1]:
        #             sum_list.append(nums[dic[0]] + nums[dics[j][0]])

        # if len(sum_list) < 1:
        #     return -1
        # else:
        #     return max(sum_list)

        def sum_digit(num):
            return sum(int(d) for d in str(num))

        digit_sum_map = defaultdict(list)

        for num in nums:
            digit_sum_map[sum_digit(num)].append(num)

        max_sum = -1

        for key in digit_sum_map:
            if len(digit_sum_map[key]) > 1:
                max1, max2 = sorted(digit_sum_map[key], reverse=True)[:2]
                max_sum = max(max_sum, max1 + max2)

        return max_sum