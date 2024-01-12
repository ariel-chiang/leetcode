# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        # record the max and min of each path, the largest diff is max-min
        def path(node: Optional[TreeNode], maxVal: int, minVal: int):
            newMax = max(maxVal, node.val)
            newMin = min(minVal, node.val)
            self.ans = max(self.ans, newMax-newMin)
            if node.left:
                path(node.left, newMax, newMin)
            if node.right:
                path(node.right, newMax, newMin)
        path(root, root.val, root.val)
        return self.ans