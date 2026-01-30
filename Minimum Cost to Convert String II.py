# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/?envType=daily-question&envId=2026-01-30
# Minimum Cost to Convert String II

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        n = len(source)
        if n != len(target):
            return -1
        
        unique_strs = set(original) | set(changed)
        str_to_id = {s: i for i, s in enumerate(unique_strs)}
        m = len(unique_strs)
        
        inf = float('inf')
        dist = [[inf] * m for _ in range(m)]
        for i in range(m):
            dist[i][i] = 0
            
        for o, c, z in zip(original, changed, cost):
            u, v = str_to_id[o], str_to_id[c]
            dist[u][v] = min(dist[u][v], z)
            
        for k in range(m):
            for i in range(m):
                if dist[i][k] == inf: continue
                for j in range(m):
                    if dist[k][j] == inf: continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.id = -1

        root = TrieNode()
        for s in original:
            node = root
            for char in s:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.id = str_to_id[s]
            
        dp = [inf] * (n + 1)
        dp[0] = 0
        
        for i in range(n):
            if dp[i] == inf:
                continue
            
            if source[i] == target[i]:
                dp[i+1] = min(dp[i+1], dp[i])
            
            node = root
            for j in range(i, n):
                char = source[j]
                if char not in node.children:
                    break
                node = node.children[char]
                
                if node.id != -1:
                    src_id = node.id
                    target_sub = target[i : j+1]
                    
                    if target_sub in str_to_id:
                        dst_id = str_to_id[target_sub]
                        
                        if dist[src_id][dst_id] != inf:
                            dp[j+1] = min(dp[j+1], dp[i] + dist[src_id][dst_id])
                            
        return dp[n] if dp[n] != inf else -1