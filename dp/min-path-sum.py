# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the 
# sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        dp = [[0 for j in range(columns)] for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                dp[i][j] += grid[i][j]
                if(i > 0 and j > 0):
                    dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                    
                elif(i > 0):
                    dp[i][j] += dp[i-1][j]
                    
                elif(j > 0):
                    dp[i][j] += dp[i][j-1]
        return dp[rows - 1][columns - 1]
                    
                