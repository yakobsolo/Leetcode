class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for p, c in adjacentPairs:
            graph[p].append(c)
            graph[c].append(p)
            indegree[c] +=1
            indegree[p] +=1
            
        visted = set()
        ans = []
        def dfs(n):
            visted.add(n)
            ans.append(n)
            for adj in graph[n]:
                if adj not in visted:
                    dfs(adj)
        
        for key in indegree:
            if indegree[key] == 1:
                dfs(key)
                break
        return ans