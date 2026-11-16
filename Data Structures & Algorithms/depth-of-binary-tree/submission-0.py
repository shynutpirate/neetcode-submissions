# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root: 
            return 0

        queue = deque()
        queue.append((root, 1))
        maxLvl = 0

        while queue:
            current, level = queue.popleft()

            if current.left:
                queue.append((current.left,level + 1))
            if current.right:
                queue.append((current.right, level + 1))
            
            maxLvl = max(level, maxLvl)
            
        return maxLvl