#!/usr/bin/env python3
"""
Module contains implementation for:
589. N-ary Tree Preorder Traversal
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""
from typing import List

class Node:
    """ Node representation."""
    def __init__(self, val=None, children=None):
        """ Initialization"""
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """ Perform Preorder Traversal of n-ary tree."""
        stack = []
        result = []

        if root is None:
            return []

        stack.append(root)
        while stack:
            current_top = stack.pop()
            if current_top:
                result.append(current_top.val)

                if current_top.children:
                    for child in reversed(current_top.children):
                        stack.append(child)
        return result

# Recursively
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        result = []
        result.append(root.val)
        for child in root.children:
            result.extend(self.preorder(child))
        return result

