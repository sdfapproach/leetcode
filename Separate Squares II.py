# https://leetcode.com/problems/separate-squares-ii/?envType=daily-question&envId=2026-01-14
# Separate Squares II

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        events.sort()
        
        history = [] 
        active_x_intervals = []
        current_area = 0.0
        prev_y = events[0][0]
        
        def get_union_width(intervals):
            if not intervals:
                return 0
            intervals.sort()
            
            total_width = 0
            curr_start, curr_end = intervals[0]
            
            for i in range(1, len(intervals)):
                next_start, next_end = intervals[i]
                if next_start < curr_end:
                    curr_end = max(curr_end, next_end)
                else:
                    total_width += (curr_end - curr_start)
                    curr_start, curr_end = next_start, next_end
            
            total_width += (curr_end - curr_start)
            return total_width

        for i, (y, type, x1, x2) in enumerate(events):
            dy = y - prev_y
            if dy > 0:
                width = get_union_width(active_x_intervals)
                current_area += width * dy
                history.append((y, current_area, width))
            
            if type == 1:
                active_x_intervals.append((x1, x2))
            else:
                active_x_intervals.remove((x1, x2))
                
            prev_y = y

        total_area = current_area
        target = total_area / 2.0
        
        prev_area = 0
        prev_y_val = events[0][0]
        
        for y, area, width in history:
            if area >= target:
                if width == 0: # 예외 처리 (혹시 모를 0 나누기 방지)
                    return float(y)
                return prev_y_val + (target - prev_area) / width
            
            prev_area = area
            prev_y_val = y
            
        return float(prev_y_val)
        
        low, high = min_y, max_y
        
        for _ in range(70):
            mid = (low + high) / 2
            current_area = get_union_area(mid)
            
            if current_area < target_area:
                low = mid
            else:
                high = mid
                
        return high