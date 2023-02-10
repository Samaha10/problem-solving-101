# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        travmap = []

        def traverse(node, counter):
            if not node:
                return
            
            if counter >= len(travmap):
                travmap.append([node.val])
            else:
                travmap[counter].append(node.val)

            traverse(node.left, counter + 1)
            traverse(node.right, counter + 1)


        traverse(root, 0)
        
        return travmap
