# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
# equals to k.

# Example 1:
# Input:nums = [1,1,1], k = 2
# Output: 2
# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1
        
        for i in nums:
            sums += i
            count += d.get(sums-k,0)
            d[sums] = d.get(sums,0) + 1
        
        return count