# https://leetcode.com/problems/construct-string-with-repeat-limit/?envType=daily-question&envId=2024-12-17
# Construct String With Repeat Limit

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        
        freq = Counter(s)
    
        max_heap = []
        for char, count in freq.items():
            heapq.heappush(max_heap, (-ord(char), count))
        
        result = []
        
        while max_heap:
            neg_ascii, count = heapq.heappop(max_heap)
            char = chr(-neg_ascii)
            
            use_count = min(count, repeatLimit)
            result.append(char * use_count)
            
            count -= use_count
            
            if count > 0:
                if not max_heap:
                    break
                next_neg_ascii, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_neg_ascii)
                
                result.append(next_char)
                next_count -= 1
                
                if next_count > 0:
                    heapq.heappush(max_heap, (next_neg_ascii, next_count))
                
                heapq.heappush(max_heap, (neg_ascii, count))
        
        return ''.join(result)