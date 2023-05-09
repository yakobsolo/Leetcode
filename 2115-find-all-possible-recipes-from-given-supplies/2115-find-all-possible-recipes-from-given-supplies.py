class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        incoming = defaultdict(int)
        q = deque()
        ans = []
        i = 0
        for ing in ingredients:
            for e in ing:
                graph[e].append(recipes[i])
                incoming[recipes[i]] +=1
        
            i+=1
        
        for s in supplies:
            q.append(s)
        
        while q:
            top = q.popleft()
            if top in recipes: ans.append(top)
            
            for ingr in graph[top]:
                incoming[ingr] -=1
                
                if incoming[ingr] == 0:
                    q.append(ingr)
        
        return ans
            