from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
		#Code here
		visted = set()

		def dfs(n, p):
		    visted.add(n)
		    for child in adj[n]:
		        if child == p: continue
		        if child not in visted:
		            if dfs(child, n): return 1
		        else:
		            return 1
		    return 0
		
		for i in range(V):
		    if i not in visted and dfs(i, v+1):
		        return 1
		return 0
		    
