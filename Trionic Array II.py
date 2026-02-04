# https://leetcode.com/problems/trionic-array-ii/?envType=daily-question&envId=2026-02-04
# Trionic Array II

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 4:
            return 0

        P = [0] * n
        P[0] = nums[0]
        for i in range(1, n):
            P[i] = P[i-1] + nums[i]

        def get_sum(start, end):
            if start == 0:
                return P[end]
            return P[end] - P[start-1]

        L = [0] * n
        L[0] = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                L[i] = nums[i] + max(0, L[i-1])
            else:
                L[i] = nums[i]

        R = [0] * n
        R[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                R[i] = nums[i] + max(0, R[i+1])
            else:
                R[i] = nums[i]

        global_max = -float('inf')
        found = False

        i = 1
        while i < n - 2:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                p = i
                j = i + 1
                valid_q = False
                
                while j < n - 1:
                    if nums[j] < nums[j-1]:
                        if nums[j] < nums[j+1]:
                            q = j
                            
                            current_sum = L[p-1] + get_sum(p, q) + R[q+1]
                            if current_sum > global_max:
                                global_max = current_sum
                                found = True
                            
                            i = q 
                            valid_q = True
                            break
                        
                        j += 1
                    else:
                        i = j - 1
                        break
                
                if not valid_q:
                    if i == p: 
                        i += 1
            else:
                i += 1

        return global_max if found else 0