# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #This was a pretty text book problem and I did it the easy way
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        if val < root.val:
            if root.left:
                self.insertIntoBST(root.left, val)
                return root
            root.left = TreeNode(val)
            return root
        if root.right:
            self.insertIntoBST(root.right, val)
            return root
        root.right = TreeNode(val)
        return root