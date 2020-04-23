# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a 
# value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal 
# displays the value of the node first, then traverses node.left, then traverses node.right.)

# Example 1:
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = None
        for i in preorder:
            root = self.addNode(i, root)
        
        return root
            
    def addNode(self, nodeval, root):
        if(not root):
            root = TreeNode(nodeval)
            return root
            
        if(root.val > nodeval):
            root.left = self.addNode(nodeval, root.left)
        
        else:
            root.right = self.addNode(nodeval, root.right)
            
        return root