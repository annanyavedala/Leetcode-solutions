# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        di={}
        def level(root, d):
            nonlocal di
            if root is None:
                return
            if d in di:
                di[d].append(root.val)
            else:
                di[d]=[root.val]
            if root.left:
                level(root.left, d+1)
            if root.right:
                level(root.right, d+1)
            return
        l=[]
        level(root, 0)
        for key, val in di.items():
            l.append(val[-1])
        return l
            
            
        
        
                
        