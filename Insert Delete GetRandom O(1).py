# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=daily-question&envId=2024-01-16
# Insert Delete GetRandom O(1)

class RandomizedSet:

    def __init__(self):
        self.num_set = []
        return None

    def insert(self, val: int) -> bool:
        num_set = self.num_set
        
        if val not in num_set:
            num_set.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        num_set = self.num_set
        
        if val in num_set:
            num_set.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        num_set = self.num_set

        return random.choice(num_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()