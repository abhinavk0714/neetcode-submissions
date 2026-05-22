class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig = image[sr][sc]
        # if orig img at [sr, sc] already equals color, then return
        if orig == color:
            return image

        ROW = len(image)
        COL = len(image[0])
        
        def dfs(row, col):
            if row < 0 or row >= ROW or col < 0 or col >= COL or image[row][col] != orig:
                return
            
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        dfs(sr, sc)
        return image