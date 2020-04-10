# Given a positive integer n, find the least number of perfect square numbers 
# (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2:
            return n
        queue = []
        toCheck = [n]
        level = 0
        for i in range(1,n):
            if(i**2 > n):
                break
            queue.append(i**2)
        
        while toCheck:
            level += 1
            temp = []
            for i in toCheck:
                for j in queue:
                    if(i == j):
                        return level
                    if(i < j):
                        break
                    temp.append(i - j)
            toCheck = temp
        return level