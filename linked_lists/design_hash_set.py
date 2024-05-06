#!/usr/bin/env python3
"""
Module contains implementation for:
705. Design HashSet
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

    void add(key) Inserts the value key into the HashSet.
    bool contains(key) Returns whether the value key exists in the HashSet or not.
    void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
class MyHashSet:

    def __init__(self):
        self.data = [False] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]

#ALTERNATIVE IMPLEMENTATION
# Using Linked List
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for i in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        current = self.set[index]

        # current holds dummy node that's why we check current.next
        while current.next:
            # If already exists
            if current.next.key == key:
                return
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        current = self.set[index]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        current = self.set[index].next
        
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

def test_my_hash_set():
    hash_set = MyHashSet()

    # Test adding elements
    hash_set.add(1)
    hash_set.add(2)
    hash_set.add(3)

    # Test contains method
    assert hash_set.contains(1) == True
    assert hash_set.contains(2) == True
    assert hash_set.contains(3) == True
    assert hash_set.contains(4) == False

    # Test removing elements
    hash_set.remove(2)

    assert hash_set.contains(2) == False
    assert hash_set.contains(1) == True
    assert hash_set.contains(3) == True
    assert hash_set.contains(4) == False

    # Test adding duplicate element
    hash_set.add(1)

    assert hash_set.contains(1) == True

    print("All tests passed!")

test_my_hash_set()

