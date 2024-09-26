# https://leetcode.com/problems/my-calendar-i/?envType=daily-question&envId=2024-09-26
# My Calendar I

class MyCalendar:

    def __init__(self):
        
        self.booked_list = []

    def book(self, start: int, end: int) -> bool:
        
        for booked in self.booked_list:

            if start < booked[1] and end > booked[0]:
                return False
            
        self.booked_list.append([start, end])
        
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)