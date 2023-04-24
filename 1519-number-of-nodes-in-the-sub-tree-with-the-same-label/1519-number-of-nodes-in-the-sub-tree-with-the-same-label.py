class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0]*n
        
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(idx, parent):
            count= collections.Counter()
            for child in graph[idx]:
                if child!= parent:
                    count+= dfs(child, idx)
            count[labels[idx]] +=1
            ans[idx] = count[labels[idx]]
            return count
            
        dfs(0, -1)
        return ans