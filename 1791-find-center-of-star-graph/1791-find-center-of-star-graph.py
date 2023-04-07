class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        leng = len(edges)
        graph = [0]*(leng+2)
        for i in range(leng):
            temp = edges[i]
            first, second = temp[0], temp[1]
            graph[first] +=1
            graph[second] +=1
        return graph.index(max(graph))