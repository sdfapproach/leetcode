# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/?envType=daily-question&envId=2024-04-08
# Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = deque(students)
        sandwiches_stack = deque(sandwiches)
        
        while sandwiches_stack:
            top_sandwich = sandwiches_stack[0]
            if top_sandwich in students_queue:
                while students_queue[0] != top_sandwich:
                    students_queue.append(students_queue.popleft())
                students_queue.popleft()
                sandwiches_stack.popleft()
            else:
                break
        
        return len(students_queue)