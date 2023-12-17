# https://leetcode.com/problems/destination-city/description/?envType=daily-question&envId=2023-12-15
# Destination City

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        # dep = [dep[0] for dep in paths]
        # des = [des[1] for des in paths]

        # for city in des:
        #     if city not in dep:
        #         return city

        dep, des = zip(*paths)

        for city in des:
            if city not in dep:
                return city