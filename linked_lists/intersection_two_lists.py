#!/usr/bin/env python3
"""
Module contains implementation for:
160. Intersection of Two Linked Lists
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB

        while currentA != currentB:
            #If we reach to end of a list-we reset the pointer to the othe list
            # That way we traverse the list still having elems(longer list) with 2 pointers
            if currentA is None:
                currentA = headB
            else:
                currentA = currentA.next

            if currentB is None:
                currentB = headA
            else:
                currentB = currentB.next
        return currentA

#Different approach
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currentA = headA
        currentB = headB

        visited = set()
        while currentA:
            visited.add(currentA)
            currentA = currentA.next

        while currentB:
            if currentB in visited:
                return currentB
            currentB = currentB.next
        return None


# geeks for geeks implementation
# utilzes set
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(node):
    current = node
    while current:
        print(current.data, end=" ")
        current = current.next
    print("")

def get_intersection_node(node1, node2):
    visited = set()

    # Traverse the first list and store the visited nodes
    while node1:
        visited.add(node1)
        node1 = node1.next

    # Traverse the second list and check if any node is visited
    while node2:
        if node2 in visited:
            return node2
        node2 = node2.next

    return None

# List 1
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(6)
list1.next.next.next.next.next.next = ListNode(7)

# List 2
list2 = ListNode(10)
list2.next = ListNode(9)
list2.next.next = ListNode(8)
list2.next.next.next = list1.next.next.next

print("List 1:")
print_list(list1)
print("List 2:")
print_list(list2)

intersection_node = get_intersection_node(list1, list2)
print("Intersection node data:", intersection_node.data if intersection_node else None)
