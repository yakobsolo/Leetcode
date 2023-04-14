class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_ = defaultdict(list)
        i= 0
        for adj in graph:
            graph_[i] += adj
            i+=1
        ans = []
        visted = set()
        def dfs(node, path):
            
            path.append(node)
            visted.add(node)
            
            for adj in graph[node]:
                if adj not in visted:
                    dfs(adj, path)
                    top = path.pop()
                    visted.discard(top)
                    
            if node == i-1:
                ans.append(path[:])
        dfs(0, [])
        return ans