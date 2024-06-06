# https://leetcode.com/problems/hand-of-straights/?envType=daily-question&envId=2024-06-06
# Hand of Straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        count = Counter(hand)

        for card in hand:
            if count[card] == 0:
                continue
            for i in range(groupSize):
                if count[card + i] <= 0:
                    return False
                count[card + i] -= 1

        return True