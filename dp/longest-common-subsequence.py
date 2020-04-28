# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
# without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" 
# is not). A common subsequence of two strings is a subsequence that is common to both strings.
# If there is no common subsequence, return 0.
# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]
        
        
        for i in range(len(text2)+1):
            for j in range(len(text1)+1):
                if(i==0 or j==0):
                    dp[i][j] = 0
                elif(text2[i-1] == text1[j-1]):
                     dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[len(text2)][len(text1)]