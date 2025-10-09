# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/?envType=daily-question&envId=2025-10-09
# Find the Minimum Amount of Time to Brew Potions

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        
        sumSkill = sum(skill)
        prevWizardDone = sumSkill * mana[0]

        for j in range(1, len(mana)):
            prevPotionDone = prevWizardDone
            for i in range(len(skill) - 2, -1, -1):
                prevPotionDone -= skill[i + 1] * mana[j - 1]
                prevWizardDone = max(prevPotionDone,
                                    prevWizardDone - skill[i] * mana[j])
            prevWizardDone += sumSkill * mana[j]

        return prevWizardDone