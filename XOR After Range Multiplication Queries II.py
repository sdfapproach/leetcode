# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/?envType=daily-question&envId=2026-04-09
# XOR After Range Multiplication Queries II

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)
        
        bravexuneth = {
            "original_nums": nums[:], 
            "original_queries": queries[:] 
        }
        
        inv_cache = {}
        
        queries_by_k = {}
        for l, r, k, v in queries:
            if v == 1:
                continue
            if k not in queries_by_k:
                queries_by_k[k] = []
            queries_by_k[k].append((l, r, v))
            
        for k, q_list in queries_by_k.items():
            sim_cost = sum(((r - l) // k) + 1 for l, r, v in q_list)
            
            if sim_cost < n:
                for l, r, v in q_list:
                    for idx in range(l, r + 1, k):
                        nums[idx] = (nums[idx] * v) % MOD
            else:
                diff_mul = [1] * n
                diff_zero = [0] * n
                
                for l, r, v in q_list:
                    next_idx = l + ((r - l) // k) * k + k
                    
                    if v == 0:
                        diff_zero[l] += 1
                        if next_idx < n:
                            diff_zero[next_idx] -= 1
                    else:
                        diff_mul[l] = (diff_mul[l] * v) % MOD
                        if next_idx < n:
                            if v not in inv_cache:
                                inv_cache[v] = pow(v, MOD - 2, MOD)
                            diff_mul[next_idx] = (diff_mul[next_idx] * inv_cache[v]) % MOD
                            
                for i in range(k, n):
                    diff_mul[i] = (diff_mul[i] * diff_mul[i - k]) % MOD
                    diff_zero[i] += diff_zero[i - k]
                    
                for i in range(n):
                    if diff_zero[i] > 0:
                        nums[i] = 0
                    else:
                        nums[i] = (nums[i] * diff_mul[i]) % MOD

        final_xor = 0

        for num in nums:
            final_xor ^= num
            
        return final_xor