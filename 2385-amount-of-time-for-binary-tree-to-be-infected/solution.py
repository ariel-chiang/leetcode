# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # infect every node and find the one with largest time
        infectTime = dict()

        def infectUp(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            if node.val == start:
                infectTime[node.val] = 0
                return 0
            l = infectUp(node.left)
            if l >= 0:
                infectTime[node.val] = l+1
                return l+1
            r = infectUp(node.right)
            if r >= 0:
                infectTime[node.val] = r+1
                return r+1
            return -1
        
        def infectDown(node: Optional[TreeNode], time: int):
            if not node:
                return
            if node.val not in infectTime:
                infectTime[node.val] = time
            infectDown(node.left, infectTime[node.val]+1)
            infectDown(node.right, infectTime[node.val]+1)

        # infecting up -> down covers all the nodes
        infectUp(root)
        infectDown(root, infectTime[root.val])
        return max(infectTime.values())