class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visits = set()
        max_area = 0
        

        def dfs(r,c):

            if (min(r,c) < 0 or
                r==rows or c>= cols or 
                (r,c) in visits or 
                grid[r][c]==0):
                return 0
            

            
            visits.add((r,c))
            area =1

            for dr,dc in directions:
                area+=dfs(r+dr, c + dc)
            
            return area
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visits:
                    area = dfs(r,c)
                    max_area = max(max_area,area)
        
        return max_area
