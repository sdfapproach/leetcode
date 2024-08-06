# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/?envType=daily-question&envId=2024-08-06
# Minimum Number of Pushes to Type Word II

class Solution:
    def minimumPushes(self, word: str) -> int:
        
        freq = Counter(word)
    
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
        
        presses = 0
        current_press = 1
        current_key_index = 0
        key_distribution = [[] for _ in range(8)]

        for char, count in sorted_chars:
            key_distribution[current_key_index].append((char, count))
            current_key_index = (current_key_index + 1) % 8

        for i, key in enumerate(key_distribution):
            press_count = 1
            for char, count in key:
                presses += press_count * count
                press_count += 1
        
        return presses