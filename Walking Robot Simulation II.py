# https://leetcode.com/problems/walking-robot-simulation-ii/?envType=daily-question&envId=2026-04-07
# Walking Robot Simulation II

class Robot:

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0
        
        self.dirs = ["East", "North", "West", "South"]
        self.moves = [(1,0), (0,1), (-1,0), (0,-1)]
        
        self.cycle = 2 * (width + height) - 4

    def step(self, num):
        if self.cycle == 0:
            return
        
        num %= self.cycle
        
        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3
            return
        
        while num > 0:
            dx, dy = self.moves[self.dir]
            nx, ny = self.x + dx, self.y + dy
            
            if not (0 <= nx < self.w and 0 <= ny < self.h):
                self.dir = (self.dir + 1) % 4
                continue
            
            self.x, self.y = nx, ny
            num -= 1

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return self.dirs[self.dir]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()