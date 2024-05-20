#!/usr/bin/env python3
"""
Module contains implementation for:
flip a binary tree towards the right direction in a clockwise manner.
"""
# Approach 1 -Recursive
"""
    Identify the leftmost node.
    Make its parent its right child.
    Make its right sibling its left child.
    Recursively apply the flip operation for all leftmost nodes.
"""
from queue import Queue
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def flipBinaryTree(root):

	if root is None:
		return root

	if (root.left is None and
		root.right is None):
		return root

	flippedRoot = flipBinaryTree(root.left)

	root.left.left = root.right
	root.left.right = root
	root.left = root.right = None

	return flippedRoot

#level order traversal line by line
def printLevelOrder(root):

	if root is None:
		return

	q = Queue()

	q.put(root)

	while(True):
		nodeCount = q.qsize()
		if nodeCount == 0:
			break

		while nodeCount > 0:
			node = q.get()
			print(node.data, end=" ")
			if node.left is not None:
				q.put(node.left)
			if node.right is not None:
				q.put(node.right)
			nodeCount -= 1

		print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print("Level order traversal of given tree")
printLevelOrder(root)

root = flipBinaryTree(root)

print("\nLevel order traversal of the flipped tree")
printLevelOrder(root)

# Iterative Approch
from collections import deque

class Node:
	# Constructor to create
	# a new node
	def __init__(self, key):
		# Initialize node data
		self.data = key
		self.left = None
		self.right = None

def flipBinaryTree(root):
	# Initialization of pointers
	curr = root
	next = None
	temp = None
	prev = None

	# Iterate through all left nodes
	while(curr):
		next = curr.left
		# Swap nodes now, need temp to keep the previous right child
		curr.left = temp
		# Store curr's right child
		temp = curr.right
		# Make prev as curr's right child
		curr.right = prev
		prev = curr
		curr = next
	return prev

def printLevelOrder(root):
	if (root == None):
		return
	q = deque()
	q.append(root)
	while (1):
		nodeCount = len(q)
		if (nodeCount == 0):
			break
		while (nodeCount > 0):
			node = q.popleft()
			print(node.data, end = " ")
			if (node.left != None):
				q.append(node.left)
			if (node.right != None):
				q.append(node.right)
			nodeCount -= 1
		print()

if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.right.left = Node(4)
	root.right.right = Node(5)

	print("Level order traversal of given tree")
	printLevelOrder(root)

	root = flipBinaryTree(root)

	print("\nLevel order traversal of the flipped tree")
	printLevelOrder(root)
