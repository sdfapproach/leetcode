# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/?envType=daily-question&envId=2025-08-03
# Maximum Fruits Harvested After at Most K Steps

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        
        max_pos = max(startPos, fruits[-1][0])
        cnt = [0]*(1+max_pos)
        
        for p, a in fruits:
            cnt[p] = a
        prefix = [0]

        for x in cnt:
            prefix.append(prefix[-1]+x)
        result = 0
        
        for left_dist in range(min(startPos, k)+1):
            right_dist = max(k-2*left_dist, 0)            
            left, right = startPos-left_dist, min(startPos+right_dist, max_pos)
            result = max(result, prefix[right+1]-prefix[left])

        for right_dist in range(min(max_pos-startPos, k)+1):
            left_dist = max(k-2*right_dist, 0) 
            left, right = max(startPos-left_dist, 0), startPos+right_dist
            result = max(result, prefix[right+1]-prefix[left])

        return result