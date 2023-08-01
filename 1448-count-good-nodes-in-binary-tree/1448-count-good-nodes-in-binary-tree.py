# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def check(root, maxi):
            nonlocal count
            
            if root:
                if(maxi<=root.val):
                    count+=1
                maxi=max(root.val, maxi)
            if root.left:
                check(root.left, maxi)
            if root.right:
                check(root.right, maxi)
            return
        
        check(root, -1000000000)
        return count
        
                
                
                
            
            
        
        
        
            
        