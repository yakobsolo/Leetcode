class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted = set()
        
        def dfs(node):
            visted.add(node)
            for n in rooms[node]:
                if n not in visted:
                    dfs(n)
        dfs(0)
        if len(visted) == len(rooms):
            return True
        else:
            return False