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
class Solution:
    def isidenticalStructure(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return self.isidenticalStructure(p.left, q.left) and self.isidenticalStructure(p.right, q.right)

