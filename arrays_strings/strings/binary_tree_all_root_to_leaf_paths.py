#!/usr/bin/env python3
"""
Module contains implementation for:
    257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:

Input: root = [1]
Output: ["1"]
"""
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        result = []
        stack = [(root, str(root.val))]  # Start with the root node and its key
        
        while stack:
            node, path = stack.pop()
            
            # If it's a leaf node, append the path to the result
            if not node.left and not node.right:
                result.append(path)
            
            # Push left child node to stack if exists
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            # Push right child node to stack if exists
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
        
        return result


