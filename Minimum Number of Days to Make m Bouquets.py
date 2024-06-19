# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/?envType=daily-question&envId=2024-06-19
# Minimum Number of Days to Make m Bouquets

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay) < m * k:
            return -1
        
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
                
                if bouquets >= m:
                    return True
            return False
        
        left, right = 1, max(bloomDay)
        
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left