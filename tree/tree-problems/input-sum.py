# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST 
# such that their sum is equal to the given target.
# Example 1:

# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
# Target = 9
# Output: True

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if (not root):
            return False
        val = root.val
        visited = []
        qu = []
        qu.append(root)
        while (not len(qu) == 0):
            temp = qu.pop(0)
            if(temp.val in visited):
                return True
            else:
                visited.append(k - temp.val)
            if(temp.left):
                qu.append(temp.left)
            if(temp.right):
                qu.append(temp.right)
        return False
            