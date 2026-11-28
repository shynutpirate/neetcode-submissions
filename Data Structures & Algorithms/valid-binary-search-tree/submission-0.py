# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverse(self, left, right, curr) -> bool:

            if not curr: return True

            if (curr.val <= left) or (curr.val >= right):
                return False
            
            return self.traverse(left, curr.val, curr.left) and self.traverse(curr.val, right, curr.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            return self.traverse(float('-inf'), float('inf'), root)
        
        
        