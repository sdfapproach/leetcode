# https://leetcode.com/problems/longest-happy-string/?envType=daily-question&envId=2024-10-16
# Longest Happy String

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        heap = []
        if a > 0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))
        
        result = []
        
        while heap:
            first_count, first_char = heappop(heap)
            
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                if not heap:
                    break
                second_count, second_char = heappop(heap)
                result.append(second_char)
                second_count += 1
                if second_count != 0:
                    heappush(heap, (second_count, second_char))
                
                heappush(heap, (first_count, first_char))
            else:
                result.append(first_char)
                first_count += 1
                if first_count != 0:
                    heappush(heap, (first_count, first_char))
        
        return ''.join(result)