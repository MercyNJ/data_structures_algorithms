#!/usr/bin/env python3
"""
Module contains implementation for:
What is n-array tree?

An n-ary tree is a hierarchical data structure where each node can have at most n children, accommodating varying degrees of branching in the tree.

Implmentation of n-array tree:
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


def print_tree(root, level=0):
    if root is None:
        return
    print("  " * level + root.data)
    if root.children:
        for child in root.children:
            print_tree(child, level + 1)


# Example usage:
if __name__ == "__main__":
    # Creating nodes
    ceo = TreeNode("CEO")
    cto = TreeNode("CTO")
    cfo = TreeNode("CFO")
    cmo = TreeNode("CMO")

    # Connecting nodes
    ceo.add_child(cto)
    ceo.add_child(cfo)
    ceo.add_child(cmo)

    eng = TreeNode("Engineering")
    pm = TreeNode("Project Management")
    finance = TreeNode("Finance")
    sales = TreeNode("Sales")

    cto.add_child(eng)
    cto.add_child(pm)
    cfo.add_child(finance)
    cmo.add_child(sales)

    devops = TreeNode("DevOps")
    accounting = TreeNode("Accounting")
    hr = TreeNode("HR")
    marketing = TreeNode("Marketing")

    eng.add_child(devops)
    sales.add_child(accounting)
    sales.add_child(hr)
    sales.add_child(marketing)

    # Printing tree
    print_tree(ceo)
