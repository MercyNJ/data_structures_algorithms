#!/usr/bin/env python3
"""
Module contains implementation for:
706. Design HashMap
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

    MyHashMap() initializes the object with an empty map.
    void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
    int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
    void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
"""
# Solution has a Time Limit Exceeded error

class ListNode:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(10**6)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.map)
        current = self.map[index]

        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        current.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = key % len(self.map)
        current = self.map[index]

        while current.next:
            if current.next.key == key:
                return current.next.value
            current.next = current.next.next
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        current = self.map[index]

        # If the node to be removed is the 1st one
        while current and current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
