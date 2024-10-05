# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/?envType=daily-question&envId=2024-10-04
# Divide Players Into Teams of Equal Skill

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()

        half = len(skill) // 2

        skill_front = skill[0:half]
        skill_back = skill[half:]

        check = skill_front[0] + skill_back[-1]

        num = 0

        for i in range(half):
            if check == (skill_front[i] + skill_back[half-1-i]):
                num += skill_front[i] * skill_back[half-1-i]
            else:
                return -1

        return num