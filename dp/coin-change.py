# You are given coins of different denominations and a total amount of money. Write a function to compute the number of 
# combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# Example 3:
# Input: amount = 10, coins = [10] 
# Output: 1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for i in range(amount + 1)] for i in range(len(coins) + 1)]
        
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if(i==0 and j==0):
                    dp[i][j] = 1
                elif(i==0):
                    dp[i][j] = 0
                elif(j==0):
                    dp[i][j] = 1
                else:
                    if(j >= coins[i-1]):
                        dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
                        
        return dp[-1][-1]