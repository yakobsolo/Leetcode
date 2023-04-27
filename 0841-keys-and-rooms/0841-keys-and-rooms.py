class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visted = set()
        visted.add(0)
        queue = deque()
        queue += rooms[0]
        while queue:
            temp = len(queue)
            for i in range(temp):
                cur = queue.popleft()
                if cur not in visted:
                    queue+= rooms[cur]
                visted.add(cur)
        return True if len(visted) == len(rooms) else False
            