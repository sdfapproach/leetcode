# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/?envType=daily-question&envId=2026-02-27
# Minimum Operations to Equalize Binary String

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        
        n = len(s)
        cnt0 = s.count('0')
        
        if cnt0 == 0:
            return 0
            
        parent = list(range(n + 3))
        
        def find(i):
            curr = i
            while parent[curr] != curr:
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr
            
        q = deque([(cnt0, 0)])
        parent[cnt0] = find(cnt0 + 2)
        
        while q:
            cur, steps = q.popleft()
            
            if cur == 0:
                return steps
                
            L = cur + k - 2 * min(cur, k)
            R = cur + k - 2 * max(0, k - n + cur)
            
            curr_val = find(L)
            
            while curr_val <= R:
                if curr_val == 0:
                    return steps + 1
                    
                q.append((curr_val, steps + 1))
                
                parent[curr_val] = find(curr_val + 2)
                curr_val = find(curr_val)
                
        return -1