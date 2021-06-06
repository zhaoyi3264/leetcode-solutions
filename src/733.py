class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        val = image[sr][sc]
        if val == newColor:
            return image
        
        m = len(image)
        n = len(image[0])
        visited = set()
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n:
                if image[i][j] == val and (i, j) not in visited:
                    visited.add((i, j))
                    image[i][j] = newColor
                    dfs(i-1, j)
                    dfs(i+1, j)
                    dfs(i, j-1)
                    dfs(i, j+1)
        
        dfs(sr, sc)
        return image
