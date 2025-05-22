# https://leetcode.com/problems/zero-array-transformation-iii/?envType=daily-question&envId=2025-05-22
# Zero Array Transformation III

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        
        total_queries = len(queries)
        n = len(nums)

        initial_coverage_delta = [0] * (n + 1)

        for l_idx, r_idx in queries:
            initial_coverage_delta[l_idx] += 1
            if r_idx + 1 < n + 1: # r_idx + 1 <= n
                initial_coverage_delta[r_idx + 1] -= 1
        
        current_initial_coverage = 0
        for i in range(n):
            current_initial_coverage += initial_coverage_delta[i]
            if nums[i] > current_initial_coverage:
                return -1

        queries_starting_at_l = [[] for _ in range(n)]
        for original_idx, (l, r) in enumerate(queries):
            queries_starting_at_l[l].append((r, original_idx))

        active_pq = [] 
        
        query_is_kept = [False] * total_queries
        num_kept_queries = 0

        kept_coverage_delta = [0] * (n + 1)
        current_kept_coverage_at_i = 0

        for i in range(n):
            for r_q, original_idx_q in queries_starting_at_l[i]:
                if not query_is_kept[original_idx_q]:
                    l_q = queries[original_idx_q][0]
                    heapq.heappush(active_pq, (-r_q, l_q, original_idx_q))
            
            current_kept_coverage_at_i += kept_coverage_delta[i]
            
            remaining_demand_at_i = nums[i] - current_kept_coverage_at_i
            
            while remaining_demand_at_i > 0:
                while active_pq and (-active_pq[0][0] < i or query_is_kept[active_pq[0][2]]):
                    heapq.heappop(active_pq)

                if not active_pq:
                    return -2 

                neg_r_best, l_best, q_idx_best = heapq.heappop(active_pq)
                r_best = -neg_r_best

                if query_is_kept[q_idx_best]:
                    continue

                query_is_kept[q_idx_best] = True
                num_kept_queries += 1
                
                l_actual = queries[q_idx_best][0]
                r_actual = r_best

                kept_coverage_delta[l_actual] += 1
                if r_actual + 1 <= n:
                    kept_coverage_delta[r_actual + 1] -= 1
                
                current_kept_coverage_at_i += 1 
                remaining_demand_at_i = nums[i] - current_kept_coverage_at_i

        return total_queries - num_kept_queries