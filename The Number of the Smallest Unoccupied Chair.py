# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/?envType=daily-question&envId=2024-10-11
# The Number of the Smallest Unoccupied Chair

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        sorted_times = sorted(enumerate(times), key=lambda x: x[1][0])
        
        available_chairs = [i for i in range(len(times))]
        occupied_chairs = []
        
        for friend, (arrival, leaving) in sorted_times:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)
            
            chair = heapq.heappop(available_chairs)
            
            if friend == targetFriend:
                return chair
            
            heapq.heappush(occupied_chairs, (leaving, chair))
        
        return -1