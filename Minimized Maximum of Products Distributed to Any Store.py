# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/?envType=daily-question&envId=2024-11-14
# Minimized Maximum of Products Distributed to Any Store

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        def can_distribute(max_products, quantities, n):
            required_stores = 0
            for quantity in quantities:
                required_stores += -(-quantity // max_products)
            return required_stores <= n

        
        left, right = 1, max(quantities)
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if can_distribute(mid, quantities, n):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer