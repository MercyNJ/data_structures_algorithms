#!/usr/bin/env python3
"""
Module contains implementation for:
1598. Crawler Log Folder
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

    "../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
    "./" : Remain in the same folder.
    "x/" : Move to the child folder named x (This folder is guaranteed to always exist).

You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder. 
"""
# logic
"""
If the stack is empty, it means the file system is already in the main folder, and no additional operations are required. Otherwise, the size of the stack represents the number of operations needed to traverse back to the main folder.
"""
from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # contain folders
        stack = []

        for op in logs:
            if op == "..":
                if stack:
                    # move to parent
                    stack.pop()
            elif op != "./": # ignore ./ ops
                folder = op[:-1] # remove trailing / 
                stack.append(folder)
        return len(stack)
