# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        di={}
        def max_sum(root, d):
            nonlocal di
            if root is None:
                return 
            if d in di:
                di[d]+=root.val
            else:
                di[d]=root.val
            if root.left:
                max_sum(root.left, d+1)
            if root.right:
                max_sum(root.right, d+1)
            return
            
        
        c=1
        max_sum(root, 1)
        if di:
            maxx=di[1]
            for key, val in di.items():
                if val>maxx:
                    maxx=val
                    c=key
        return c
                
                
            
        