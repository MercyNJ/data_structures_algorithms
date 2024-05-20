#!/usr/bin/env python3
"""
Module contains implementation for:
Check if two trees have same structure
Given two binary trees. The task is to write a program to check if the two trees are identical in structure.
The idea is to traverse both trees simultaneously following the same paths and keep checking if a node exists for both the trees or not.
If both trees are empty, return 1.
If both trees are non-empty:

    Check if left subtrees are identical.
    Check if right subtrees are identical.
    If both checks pass, return 1.
    Otherwise, return 0.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isidenticalStructure(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return self.isidenticalStructure(p.left, q.left) and self.isidenticalStructure(p.right, q.right)


def test_identical_structure():
    solution = Solution()

    # Test case 1: Trees with the same structure
    root1 = TreeNode(10)
    root1.left = TreeNode(7)
    root1.right = TreeNode(15)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(9)
    root1.right.right = TreeNode(20)

    root2 = TreeNode(100)
    root2.left = TreeNode(70)
    root2.right = TreeNode(150)
    root2.left.left = TreeNode(40)
    root2.left.right = TreeNode(90)
    root2.right.right = TreeNode(200)

    assert solution.isidenticalStructure(root1, root2) == True

    # Test case 2: Trees with different structure
    root3 = TreeNode(10)
    root3.left = TreeNode(7)
    root3.right = TreeNode(15)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(9)
    root3.right.right = TreeNode(20)

    root4 = TreeNode(100)
    root4.left = TreeNode(70)
    root4.right = TreeNode(150)
    root4.left.left = TreeNode(40)
    root4.left.right = TreeNode(90)
    root4.right.left = TreeNode(200)

    assert solution.isidenticalStructure(root3, root4) == False

    print("All test cases passed!")

test_identical_structure()
