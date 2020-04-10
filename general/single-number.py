# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        d={}
        for i in nums:
            if(i in d):
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for i in d:
            if(d[i]==1):
                return i
        return 0

# or

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res = res ^ nums[i]
        return res

# or 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x^y, nums, 0)