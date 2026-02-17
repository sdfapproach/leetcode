# https://leetcode.com/problems/binary-watch/?envType=daily-question&envId=2026-02-17
# Binary Watch

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        res = []

        for h in range(12):
            for m in range(60):
                if (h.bit_count() + m.bit_count()) == turnedOn:
                    res.append(f"{h}:{m:02d}")

        return res