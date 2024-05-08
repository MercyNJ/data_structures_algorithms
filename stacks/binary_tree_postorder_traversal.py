#!/usr/bin/env python3
"""
Module contains implementation for:
145. Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []
"""
# Recursive Approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

#Iterative Approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        result = []

        while stack:
            current_top = stack.pop()
            if current_top:
                result.insert(0, current_top.val)

                if current_top.left:
                    stack.append(current_top.left)
                if current_top.right:
                    stack.append(current_top.right)
        return result
