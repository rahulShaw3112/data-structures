# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if(not grid):
            return 0
        noi = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if(grid[i][j]=='1'):
                    noi += self.dfs(grid, i, j)
        return noi
        
    def dfs(self, grid, i, j):
        if(i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0'):
            return 0
        grid[i][j] = '0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
        return 1