class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i, v in enumerate(parent):
            graph[v].append(i)
        
        ans = 1
        def dfs(node):
            
            nonlocal ans
            if not graph[node]: return 1
            second_longest, longest = 0, 0
            
            for adj in graph[node]:
                length = dfs(adj)
                
                if s[node] != s[adj]:
                    if length>longest:
                        second_longest = longest
                        longest = length
                    elif length>second_longest:
                        second_longest = length
            ans = max(ans, longest+second_longest+1)
            return longest + 1
        dfs(0)
        return ans