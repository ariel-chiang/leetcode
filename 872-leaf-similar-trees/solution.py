# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(node: TreeNode) -> list:
            leavesList = []
            if node.left:
                leavesList.extend(leaves(node.left))
            if node.right:
                leavesList.extend(leaves(node.right))
            if not node.left and not node.right:
                leavesList.append(node.val)
            return leavesList
        return leaves(root1) == leaves(root2)