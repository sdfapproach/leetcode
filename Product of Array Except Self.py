# https://leetcode.com/problems/product-of-array-except-self/?envType=daily-question&envId=2024-03-15
# Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer = []

        product_all = 1

        for num in nums:
            product_all *= num

        for i, num in enumerate(nums):

            if num == 0:

                product = 1

                for j in range(len(nums)):
                    if i!=j:
                        product *= nums[j]

                answer.append(product)

            else:
                answer.append(product_all // num)

        return answer