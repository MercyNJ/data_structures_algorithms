#!/usr/bin/env python3
"""
Module contains implementation for:
897. Increasing Order Search Tree
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Input: root = [5,1,7]
Output: [1,null,5,null,7]
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        result = None
        current = root
        prev = None

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            new_node = TreeNode(current.val)
            if not result:
                result = new_node
            if prev:
                prev.right = new_node
            prev = new_node
            current = current.right
        return result
