class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for p, c in edges:
            graph[p].append(c)
            graph[c].append(p)
        trace = {0: -1}
        visted = set()
        apple = set()
        def dfs(node):
            
            visted.add(node)
            for child in graph[node]:
                if child not in visted:
                    trace[child] = node
                    if hasApple[child]:
                        apple.add(child)
                    dfs(child)
        dfs(0)
        path = set()
        sol = 0
        for n in apple:
            
            cur = n
            ans = 0
            while trace[cur] != -1:
                if (cur, trace[cur]) not in path:
                    ans+=1
                    
                path.add((cur, trace[cur]))
                cur = trace[cur]
            sol += ans*2
        return sol
                
            