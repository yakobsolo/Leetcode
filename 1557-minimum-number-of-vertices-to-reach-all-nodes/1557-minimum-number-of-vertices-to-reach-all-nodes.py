class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        leng = len(edges)
        for i in range(leng):
            graph[edges[i][0]].append(edges[i][1])
            
        not_ans = set()
        
        for key in graph:
            not_ans.update(set(graph[key]))
            
        ans = []  
        for i in range(n):
            if i not in not_ans:
                ans.append(i)
        return ans