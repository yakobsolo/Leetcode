class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visted = set()
        initial = image[sr][sc]
        n, m = len(image), len(image[0])
        def dfs(l, r):
            image[l][r] = color
            visted.add((l, r))
            for i in range(4):
                i, j = l+direction[i][0], r+direction[i][1]
                print(i, j)
                if i>=0 and i<n and j>=0 and j<m and ((i, j) not in visted) and image[i][j] == initial:
                    image[i][j] = color
                    print(i, j)
                    dfs(i, j)
        dfs(sr, sc)
        return image