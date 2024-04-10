# https://leetcode.com/problems/reveal-cards-in-increasing-order/?envType=daily-question&envId=2024-04-10
# Reveal Cards In Increasing Order

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck, reverse=True)
    
        final_sequence = deque()
        
        for card in sorted_deck:
            if final_sequence:
                final_sequence.appendleft(final_sequence.pop())
            final_sequence.appendleft(card)
        
        return list(final_sequence)