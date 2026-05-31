# https://leetcode.com/problems/destroying-asteroids/?envType=daily-question&envId=2026-05-31
# Destroying Asteroids

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        
        asteroids.sort()

        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid

        return True