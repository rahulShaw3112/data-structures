# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Example 1:
# Input: [1,1,1,1,1,null,1]
# Output: true

# Example 2:
# Input: [2,2,2,5,2]
# Output: false

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (not root):
            return False
        val = root.val
        qu = []
        qu.append(root)
        while (not len(qu) == 0):
            temp = qu.pop(0)
            if(not temp.val == val):
                return False
            if(temp.left):
                qu.append(temp.left)
            if(temp.right):
                qu.append(temp.right)
        return True
        