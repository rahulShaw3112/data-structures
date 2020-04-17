# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. 
# For each integer, you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if(not nums):
            return 0
        self.memo = {}
        return self.dfs(nums, 0, 0, S)
        
    def dfs(self, nums, i, s, target):
        if((i,s) in self.memo):
            return self.memo[(i,s)]
        if(i == len(nums) and s == target):
            return 1
        if(i == len(nums)):
            return 0
        
        withAdd = self.dfs(nums, i + 1, s + nums[i], target)
        withMinus = self.dfs(nums, i + 1, s - nums[i], target)
        self.memo[(i,s)] = withAdd + withMinus
        return withAdd + withMinus