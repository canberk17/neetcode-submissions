class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def memoization(r, c, rows, cols, cache):

            if r == rows or c == cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1
            

            if cache[r][c] > 0:
                return cache[r][c]

            cache[r][c] = (
                memoization(r + 1, c, rows, cols, cache) +
                memoization(r, c + 1, rows, cols, cache)
            )

            return cache[r][c]
        

        return memoization(0,0,len(obstacleGrid),len(obstacleGrid[0]),[[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))])