# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both nodes are None --> return True
        if p is None and q is None:
            return True

        # either one None --> return False
        if p is None or q is None:
            return False

        # values are differ --> return False
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left))
