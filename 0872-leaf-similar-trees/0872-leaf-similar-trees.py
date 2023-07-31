# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
            
        l1=[]
        l2=[]
        def dfs1(node):
            nonlocal l1
            if node:
                if not node.left and not node.right:
                    l1.append(node.val)
                dfs1(node.left)
                dfs1(node.right)
        def dfs2(node):
            nonlocal l2
            if node:
                if not node.left and not node.right:
                    l2.append(node.val)
                dfs2(node.left)
                dfs2(node.right)
        
        # x=dfs(root1, [])
        dfs1(root1)
        dfs2(root2)
        return l1==l2
            
            
            
        
        
        