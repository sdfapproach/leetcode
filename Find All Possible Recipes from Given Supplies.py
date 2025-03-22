# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/?envType=daily-question&envId=2025-03-21
# Find All Possible Recipes from Given Supplies

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        indegree = {recipe: 0 for recipe in recipes}
        
        for r, ingr_list in zip(recipes, ingredients):
            indegree[r] = len(ingr_list)
            for ingr in ingr_list:
                graph[ingr].append(r)
                
        q = deque(supplies)
        result = []
        
        while q:
            item = q.popleft()
            for r in graph[item]:
                indegree[r] -= 1
                if indegree[r] == 0:
                    result.append(r)
                    q.append(r)
        
        return result