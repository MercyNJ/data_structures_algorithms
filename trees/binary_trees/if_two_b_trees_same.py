#!/usr/bin/env python3
"""
Module contains implementation for:
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
# Approach 1 - Recursion

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return ((p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

def test_isSameTree():
    solution = Solution()

    # Test case 1: p = [1,2,3], q = [1,2,3]
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    assert solution.isSameTree(p1, q1) == True

    # Test case 2: p = [1,2], q = [1,null,2]
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    assert solution.isSameTree(p2, q2) == False

    # Test case 3: p = [1,2,1], q = [1,1,2]
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)

    q3 = TreeNode(1)
    q3.left = TreeNode(1)
    q3.right = TreeNode(2)

    assert solution.isSameTree(p3, q3) == False

    print("All test cases passed!")

test_isSameTree()

# Approach 2 - Iterative using stack
"""
Initialize stack with corresponding nodes.
Iterate over stack.
Pop node pairs.
If both None, continue.
If one None while other not, return False.
If values different, return False.
Append left and right children for comparison.
Return True if loop completes without returning False.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node_p, node_q = stack.pop()
            if not node_p and not node_q:
                continue
            if not node_p or not node_q:
                return False
            if node_p.val != node_q.val:
                return False
            stack.append((node_p.left, node_q.left))
            stack.append((node_p.right, node_q.right))
        return True
