# Find the sum of all left leaves in a given binary tree.
# Example:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    sum = 0
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.findSum(root, '')
        return self.sum
    
    def findSum(self, root, direction):
        if(not root):
            return
        if(not root.left and not root.right):
            if(direction == 'left'):
                self.sum += root.val
                return
        self.findSum(root.left, 'left')
        self.findSum(root.right, 'right')