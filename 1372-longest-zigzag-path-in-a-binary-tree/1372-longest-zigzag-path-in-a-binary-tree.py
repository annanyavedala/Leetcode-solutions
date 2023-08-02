# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxx1=0
        def longest(root, direction, maxx):
            nonlocal maxx1
            if root is None:
                return
            maxx1=max(maxx1, maxx)
            if direction=='R':
                longest(root.left, 'L', 1+maxx)
                longest(root.right, 'R', 1)
            if direction=='L':
                longest(root.right, 'R', 1+maxx)
                longest(root.left, 'L', 1)
            return
        longest(root, 'L', 0)
        longest(root, 'R', 0)
        return maxx1
            
            
        