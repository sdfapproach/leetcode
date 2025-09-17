# https://leetcode.com/problems/design-a-food-rating-system/?envType=daily-question&envId=2025-09-17
# Design a Food Rating System

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.info = {}
        self.heaps = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.info[f] = [c, r]
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.info[food]
        self.info[food][1] = newRating
        heapq.heappush(self.heaps[c], (-newRating, food))  # lazy insert

    def highestRated(self, cuisine: str) -> str:
        h = self.heaps[cuisine]
        while h:
            neg_r, name = h[0]
            if -neg_r == self.info[name][1]:
                return name
            heapq.heappop(h)
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)