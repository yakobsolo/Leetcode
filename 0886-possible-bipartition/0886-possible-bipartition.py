class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])
        bi = [0]*(n+1)
        visted = set()
        
        def bipirtite(node, prev):
            bi[node] = prev
            visted.add(node)
            for neighbor in graph[node]:
                if neighbor not in visted:
                    if not bipirtite(neighbor, -prev):
                        return False
                else:
                    if bi[node] == bi[neighbor]:
                        return False

            return True

        for i in range(1, n+1):
            if i not in visted and not bipirtite(i, 1):
                return False
        return True