# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/?envType=daily-question&envId=2025-07-26
# Maximize Subarrays After Removing One Conflicting Pair

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        m = len(conflictingPairs)
        
        pairs = [(min(a,b), max(a,b)) for a,b in conflictingPairs]
        pairs.sort(key=lambda x: (-x[0], x[1]))
        
        import heapq
        pq = []
        idx = 0
        first = [n+1]*(n+2)
        second= [n+1]*(n+2)
        
        for l in range(n, 0, -1):
            while idx < m and pairs[idx][0] >= l:
                heapq.heappush(pq, pairs[idx][1])
                idx += 1
            if pq:
                first[l] = pq[0]
                if len(pq) >= 2:
                    first_m = heapq.heappop(pq)
                    second[l] = pq[0]
                    heapq.heappush(pq, first_m)
        
        base = sum(first[l]-l for l in range(1, n+1))
        
        delta = [second[l] - first[l] for l in range(n+1)]
        group = {}
        for l in range(1, n+1):
            M = first[l]
            if M <= n:
                group.setdefault(M, []).append(l)
        
        pref = {}
        for M, Ls in group.items():
            Ls.sort()
            ps = [0]
            for l in Ls:
                ps.append(ps[-1] + delta[l])
            pref[M] = (Ls, ps)
        
        best_gain = 0
        for a,b in conflictingPairs:
            m0, M0 = min(a,b), max(a,b)
            if M0 not in pref:
                continue
            Ls, ps = pref[M0]
            cnt = bisect.bisect_right(Ls, m0)
            best_gain = max(best_gain, ps[cnt])
        
        return base + best_gain