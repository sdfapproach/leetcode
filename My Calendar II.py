# https://leetcode.com/problems/my-calendar-ii/?envType=daily-question&envId=2024-09-27
# My Calendar II

class MyCalendarTwo:

    def __init__(self):

        self.booked_list_1 = []
        self.booked_list_2 = []
        

    def book(self, start: int, end: int) -> bool:
        
        for booked in self.booked_list_2:
            if start < booked[1] and end > booked[0]:
                return False

        for booked in self.booked_list_1:
            if start < booked[1] and end > booked[0]:

                overlap_start = max(start, booked[0])
                overlap_end = min(end, booked[1])
                self.booked_list_2.append([overlap_start, overlap_end])

        self.booked_list_1.append([start, end])

        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)