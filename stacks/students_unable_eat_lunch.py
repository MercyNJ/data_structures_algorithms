#!/usr/bin/env python3
"""
Module contains implementation for:
1700. Number of Students Unable to Eat Lunch
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

    If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    Otherwise, they will leave it and go to the queue's end.

This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.
"""
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Initialize a queue with students' preferences
        queue = deque(students)
        # Initialize a stack with sandwiches
        stack = sandwiches[::-1]  # Reverse the sandwiches to represent the top of the stack
        # Counter for students who couldn't eat
        unable_to_eat = 0

        # Loop until either all students have eaten or none of them can eat
        while queue:
            # Check if the front student's preference matches the top sandwich
            if queue[0] == stack[-1]:
                # Remove the student from the queue and the sandwich from the stack
                queue.popleft()
                stack.pop()
                # Reset unable_to_eat counter
                unable_to_eat = 0
            else:
                # Move the student to the end of the queue
                queue.append(queue.popleft())
                # Increment unable_to_eat counter
                unable_to_eat += 1
                # If all students have moved and none could eat, break the loop
                if unable_to_eat == len(queue):
                    break

        return len(queue)
