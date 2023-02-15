# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}

        def organize_parent(node):
            if not node:
                return 
            
            if node.right:
                parent[node.right] = node
            if node.left:
                parent[node.left] = node
            
            organize_parent(node.right)
            organize_parent(node.left)
    
        organize_parent(root)

        chain1 = [p]
        chain2 = [q]

        temp1 = p
        temp2 = q

        while temp1:
            chain1.append(parent[temp1])
            temp1 = parent[temp1]
        
        while temp2:
            chain2.append(parent[temp2])
            temp2 = parent[temp2]

        i = len(chain1) - 1
        j = len(chain2) - 1

        while i >= 0 and j >= 0 and chain1[i] == chain2[j]:
            record = chain1[i]
            i -= 1
            j -= 1
        
        return record