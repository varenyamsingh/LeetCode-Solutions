# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def inorderTraversal(self, root):
        result = []
        stack = deque()
        current = root

        while current or stack:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result