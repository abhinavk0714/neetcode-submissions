class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Solved using recursive DFS

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # edge case checks
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"):
                return
            
            grid[r][c] = "0" # set the current spot to zero so we dont double check the same spot
            for dr, dc in directions:
                dfs(r + dr, c + dc) # recursively run dfs every dir from our current spot
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": # if we find a 1, run dfs on that tile, and update island count
                    dfs(r, c)
                    islands += 1
        
        return islands
