#!/usr/bin/env python3
"""
Module contains implementation for:
226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root.
"""
# Approach 1 - Iterative
"""
    If root is None, return None.
    Push root to stack.
    While stack not empty:
        Pop current node.
        Swap left and right children.
        Push non-null children to stack.
    Repeat until stack is empty.
    Return root.
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [root]
        while stack:
            current = stack.pop()
            current.left, current.right = current.right, current.left
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return root

def test_invertTree():
    solution = Solution()

    # Test case 1: Input: root = [4,2,7,1,3,6,9]
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(7)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)
    expected1 = TreeNode(4)
    expected1.left = TreeNode(7)
    expected1.right = TreeNode(2)
    expected1.left.left = TreeNode(9)
    expected1.left.right = TreeNode(6)
    expected1.right.left = TreeNode(3)
    expected1.right.right = TreeNode(1)

    # Test case 2: Input: root = []
    root3 = None
    expected3 = None
    assert solution.invertTree(root3) == expected3, "Test case 3 failed"

    print("All test cases passed!")

test_invertTree()

# Approach 2 - Recursive
"""
If root is None, return None.

- Invert left subtree recursively.
- Invert right subtree recursively.

Swap: Swap left and right subtrees.

Return root node.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        l_invert = self.invertTree(root.left)
        r_invert = self.invertTree(root.right)

        root.left = r_invert
        root.right = l_invert

        return root
