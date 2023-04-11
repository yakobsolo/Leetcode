class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                
                if isConnected[r][c] ==1:
                    cities[r+1].append(c+1)
                    
        count =0
        visted = set()
        for i in range(len(cities)):
            def dfs(c):
                visted.add(c)
                for p in cities[c]:
                    if p not in visted:
                        dfs(p)
            if i+1 not in visted:
                count +=1
                dfs(i+1)
     
        return count