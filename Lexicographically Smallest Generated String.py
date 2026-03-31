# https://leetcode.com/problems/lexicographically-smallest-generated-string/?envType=daily-question&envId=2026-03-31
# Lexicographically Smallest Generated String

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        
        n = len(str1)
        m = len(str2)
        total_len = n + m - 1
        
        word = ['?'] * total_len
        last_T = -1
        
        for i in range(total_len):
            if i < n and str1[i] == 'T':
                last_T = i
            if last_T != -1 and i - last_T < m:
                word[i] = str2[i - last_T]
                
        B1, Mod1 = 131, 10**9 + 7
        B2, Mod2 = 137, 10**9 + 9
        pow1 = [1] * (total_len + 2)
        pow2 = [1] * (total_len + 2)
        for i in range(1, total_len + 2):
            pow1[i] = (pow1[i - 1] * B1) % Mod1
            pow2[i] = (pow2[i - 1] * B2) % Mod2
            
        def build_hash(s_list):
            h1 = [0] * (len(s_list) + 1)
            h2 = [0] * (len(s_list) + 1)
            for i, c in enumerate(s_list):
                val = ord(c)
                h1[i + 1] = (h1[i] * B1 + val) % Mod1
                h2[i + 1] = (h2[i] * B2 + val) % Mod2
            return h1, h2
            
        static_h1, static_h2 = build_hash(word)
        str2_h1, str2_h2 = build_hash(list(str2))
        
        def get_static_hash(l, r):
            if l > r: return (0, 0)
            length = r - l + 1
            v1 = (static_h1[r + 1] - static_h1[l] * pow1[length]) % Mod1
            v2 = (static_h2[r + 1] - static_h2[l] * pow2[length]) % Mod2
            return (v1, v2)
            
        def get_str2_hash(l, r):
            if l > r: return (0, 0)
            length = r - l + 1
            v1 = (str2_h1[r + 1] - str2_h1[l] * pow1[length]) % Mod1
            v2 = (str2_h2[r + 1] - str2_h2[l] * pow2[length]) % Mod2
            return (v1, v2)
            
        for i in range(n):
            if str1[i] == 'T':
                if get_static_hash(i, i + m - 1) != get_str2_hash(0, m - 1):
                    return ""
                    
        q_positions = [i for i, c in enumerate(word) if c == '?']
        from bisect import bisect_right
        
        last_q = [-1] * n
        for i in range(n):
            if str1[i] == 'F':
                idx = bisect_right(q_positions, i + m - 1) - 1
                if idx >= 0 and q_positions[idx] >= i:
                    last_q[i] = q_positions[idx]
                else:
                    if get_static_hash(i, i + m - 1) == get_str2_hash(0, m - 1):
                        return ""
                        
        active_L = [[] for _ in range(total_len)]
        for i in range(n):
            if str1[i] == 'F' and last_q[i] != -1:
                k = last_q[i]
                L = k - i
                L2 = m - 1 - L
                suffix_matches = True
                if L2 > 0:
                    if get_static_hash(k + 1, i + m - 1) != get_str2_hash(L + 1, m - 1):
                        suffix_matches = False
                if suffix_matches:
                    active_L[k].append(L)
                    
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and str2[i] != str2[j]:
                j = pi[j - 1]
            if str2[i] == str2[j]:
                j += 1
            pi[i] = j
            
        adj = [[] for _ in range(m + 1)]
        for v in range(1, m + 1):
            p = pi[v - 1]
            adj[p].append(v)
            
        tin = [0] * (m + 1)
        tout = [0] * (m + 1)
        timer = 0
        stack = [0]
        state = [0] * (m + 1)
        while stack:
            u = stack[-1]
            if state[u] == 0:
                tin[u] = timer
                timer += 1
            if state[u] < len(adj[u]):
                v = adj[u][state[u]]
                state[u] += 1
                stack.append(v)
            else:
                tout[u] = timer
                stack.pop()
                
        j = 0
        for k in range(total_len):
            if word[k] != '?':
                c = word[k]
            else:
                forbidden = set()
                for L in active_L[k]:
                    if tin[L] <= tin[j] and tout[j] <= tout[L]:
                        forbidden.add(str2[L])
                        
                c = '?'
                for char_code in range(97, 123):
                    char = chr(char_code)
                    if char not in forbidden:
                        c = char
                        break
                if c == '?':
                    return ""
                word[k] = c
                
            if j == m:
                j = pi[j - 1]
            while j > 0 and str2[j] != c:
                j = pi[j - 1]
            if str2[j] == c:
                j += 1
                
        return "".join(word)