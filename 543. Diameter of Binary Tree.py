# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxi = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        if not root :
            return
        
        self.maxi = max(self.maxi, maxDepth(root.left) +   maxDepth(root.right))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        
        return self.maxi

        
def maxDepth(node):
    if not node:
            return 0
        
    return 1 + max(maxDepth(node.left), maxDepth(node.right))
        
        