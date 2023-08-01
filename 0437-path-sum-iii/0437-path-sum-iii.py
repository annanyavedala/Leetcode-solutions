# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count=0
        def sum(root, targetSum):
            nonlocal count
            if root is None:
                return 
            elif root.val==targetSum:
                count+=1
            sum(root.left, targetSum-root.val)
            sum(root.right, targetSum-root.val)
        def dfs(root, targetSum):
            if root is None:
                return
            sum(root, targetSum)
            dfs(root.left, targetSum)
            dfs(root.right, targetSum)
        dfs(root, targetSum)
        return count
    
    
    
    

            
                    
        