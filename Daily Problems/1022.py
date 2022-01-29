# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #This problem was interesting because you just had to add the left and right node but it looks more complicated
    def aux(self,node, num):
        if not node.left and not node.right:
            return int(num + str(node.val), 2)
        l = 0
        r = 0
        if node.left:
            l = self.aux(node.left, num + str(node.val))
        if node.right:
            r = self.aux(node.right, num + str(node.val))
        return l + r
            
    
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.aux(root, "")