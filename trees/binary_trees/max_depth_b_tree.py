#!/usr/bin/env python3
"""
Module contains implementation for:
Find the Maximum Depth or Height of given Binary Tree
Given a binary tree, the task is to find the height of the tree. The height of the tree is the number of vertices in the tree from the root to the deepest node.

Note: The height of an empty tree is 0 and the height of a tree with single node is 1.
"""
# Approach 1 - Recursion
"""
    Perform a depth-first search recursively.
    If the tree is empty, return 0.
    Otherwise:
        Get the node's height as max(left subtree depth, right subtree depth) + 1.
    Return the node's height.
    O(n) Complexity
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

# Approach 2 - Level order Traversal
"""
    Start with the root.
    Use a queue.
    Enqueue root.
    Initialize height counter to 0.
    While queue not empty:
    increment the height counter, dequeue the node, process the node, and enqueue its children.
    Repeat until queue empty.
    Return height counter.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        q = [root]

        if root is None:
            return 0

        while q:
            # count of nodes at current level
            nodecount = len(q)
            while nodecount > 0:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                # keep track of nodes processed at current level
                nodecount -= 1
            # after all nodes current level are traversed
            height += 1
        return height

# Above level order traversal can be rewritten as
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        height = 0
        q = [root]
        while q:
            height += 1
            level_size = len(q)
            for _ in range(level_size):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return height


