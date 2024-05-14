#!/usr/bin/env python3
"""
Module contains implementation for:
590. N-ary Tree Postorder Traversal
Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = []
        result = []
        stack.append(root)
        while stack:
            current_top = stack.pop()
            result.insert(0, current_top.val)
            if current_top.children:
                for child in current_top.children:
                    stack.append(child)
        return result

# Recursive Approach
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.children:
                stack.extend(current.children)
        return result[::-1]
