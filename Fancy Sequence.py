# https://leetcode.com/problems/fancy-sequence/?envType=daily-question&envId=2026-03-15
# Fancy Sequence

class Fancy:

    def __init__(self):
        self.seq = []
        self.add = 0
        self.mul = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        val = (val - self.add) % self.MOD
        inverse_mul = pow(self.mul, self.MOD - 2, self.MOD)
        v_base = (val * inverse_mul) % self.MOD
        
        self.seq.append(v_base)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        
        ans = (self.seq[idx] * self.mul + self.add) % self.MOD
        return ans

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)