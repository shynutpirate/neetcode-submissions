# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
     
    def sameTree(self, root1, root2) -> bool:
        if not root1 and not root2: return True
        if (root1 and not root2) or (not root1 and root2): return False
        return root1.val == root2.val and self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def traverse(root, subRoot):
            if not root: return False

            if self.sameTree(root, subRoot): return True
            return traverse(root.left, subRoot) or traverse(root.right, subRoot)
        
        return traverse(root, subRoot)

        