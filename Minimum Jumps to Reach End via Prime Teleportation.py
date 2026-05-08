# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/?envType=daily-question&envId=2026-05-08
# Minimum Jumps to Reach End via Prime Teleportation

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n <= 1:
            return 0
            
        max_val = max(nums)
        
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_val**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False
                    
        primes_present = set(x for x in nums if is_prime[x])
        
        val_to_indices = {}
        for i, num in enumerate(nums):
            if num not in val_to_indices:
                val_to_indices[num] = []
            val_to_indices[num].append(i)
            
        prime_to_indices = {p: [] for p in primes_present}
        for p in primes_present:
            for multiple in range(p, max_val + 1, p):
                if multiple in val_to_indices:
                    prime_to_indices[p].extend(val_to_indices[multiple])
                    
        q = deque([(0, 0)])
        visited = set([0])
        visited_primes = set()
        
        while q:
            curr, jumps = q.popleft()
            
            if curr == n - 1:
                return jumps
                
            for nxt in (curr - 1, curr + 1):
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, jumps + 1))
                    
            if is_prime[nums[curr]]:
                p = nums[curr]
                if p not in visited_primes:
                    visited_primes.add(p)
                    for nxt in prime_to_indices[p]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append((nxt, jumps + 1))
                            
        return -1