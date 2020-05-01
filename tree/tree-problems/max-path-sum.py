# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along 
# the parent-child connections. The path must contain at least one node and does not need to go through the root.
# Example 1:
# Input: [1,2,3]

#        1
#       / \
#      2   3
# Output: 6
# Example 2:
# Input: [-10,9,20,null,null,15,7]
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# Output: 42

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -1 * sys.maxsize
        self.helper(root)
        return self.ans
        
    def helper(self, root: TreeNode):
        if(not root):
            return 0
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        ms = max(max(left, right) + root.val, root.val)
        self.ans = max(self.ans, ms, root.val + left + right)
        
        return ms