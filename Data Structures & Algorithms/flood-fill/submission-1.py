class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols= len(image), len(image[0])

        origin = image[sr][sc]

        if origin == color:
            return image
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if (min(r,c) < 0 or r == rows or c == cols or
               image[r][c] != origin):
               return
            
            image[r][c] = color
        
            for dr,dc in directions:
                dfs(r + dr, c + dc)
        
        dfs(sr,sc)
        return image

