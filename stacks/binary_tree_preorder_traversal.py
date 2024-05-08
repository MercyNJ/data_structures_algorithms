#!/usr/bin/env python3
"""
Module contains implementation for:
144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []
"""
from typing import List, Optional

# Recursion Approach
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# Iterative Approach
"""
Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """Initialize a TreeNode."""
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """Perform pre-order traversal iteratively."""
        stack = []
        result = []

        stack.append(root)
        while stack:
            current_top = stack.pop()
            if current_top:
                result.append(current_top.val)

                if current_top.right:
                    stack.append(current_top.right)
                if current_top.left:
                    stack.append(current_top.left)
        return result

def test_preorderTraversal():
    """Test function for preorderTraversal method."""
    solution = Solution()

    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    assert solution.preorderTraversal(root1) == [1, 2, 3]

    root2 = None
    assert solution.preorderTraversal(root2) == []

    root3 = TreeNode(1)
    assert solution.preorderTraversal(root3) == [1]

    print("All test cases passed!")
test_preorderTraversal()




