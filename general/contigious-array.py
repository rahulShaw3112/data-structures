# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

# Example 1:
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
# Example 2:
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Note: The length of the given binary array will not exceed 50,000.

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:0}
        cnt = 0
        ans = 0
        for i, num in enumerate(nums, 1):
            if(num==0):
                cnt -= 1
            else:
                cnt += 1
            if(cnt in d):
                ans = max(ans, i - d[cnt])
            else:
                d[cnt] = i
        return ans
            