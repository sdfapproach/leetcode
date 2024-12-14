# https://leetcode.com/problems/continuous-subarrays/?envType=daily-question&envId=2024-12-14
# Continuous Subarrays

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        

        n = len(nums)
        maxQ = deque()
        minQ = deque()
        left = 0
        ans = 0
        
        for right in range(n):
            while maxQ and maxQ[-1] < nums[right]:
                maxQ.pop()
            maxQ.append(nums[right])
            
            while minQ and minQ[-1] > nums[right]:
                minQ.pop()
            minQ.append(nums[right])
            
            while maxQ[0] - minQ[0] > 2:
                if maxQ[0] == nums[left]:
                    maxQ.popleft()
                if minQ[0] == nums[left]:
                    minQ.popleft()
                left += 1
            
            ans += (right - left + 1)
        
        return ans