"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        #Append adds the value at the end of the list
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        #If the stack is empty we don't perform any operations, instead, we print a message
        if self.is_empty():
            return "Empty stack. Unable to pop"
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek() shows us the last value that was entered (top).
        # We use negative index to access last item inn the list
        if self.is_empty():
            return "Empty stack, nothing to peek"
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # We check the list for items and return true if it has no values
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if self.is_empty():
            print("Empty queue. Unable to deque")
            return None
        return self.items.pop()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if self.is_empty():
            print("Empty queue.")
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items)==0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements & edge Cases:

    # 1. Create a Stack object.
    stack1 = Stack()

    # 2. Add at least 4 values to the stack.
    stack1.push(1)
    stack1.push(2)
    stack1.push(3)
    stack1.push(4)

    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    print(f"Stack: {stack1.items}")
    print(f"Top element(peek): {stack1.peek()}")
    while not stack1.is_empty():
        print(f"Popped: {stack1.pop()}")
        print(f"Stack: {stack1.items}")

    # 5. Show what happens when pop() is used on an empty stack.
    print(f"Using pop() on an empty stack: {stack1.pop()}")

    # 6. Show what happens when peek() is used on an empty stack.
    print(f"Using peek() on an empty stack: {stack1.peek()}")

    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
    stack2 = Stack()
    stack2.push(7)
    print(f"Pushed 7. Stack: {stack2.items}")
    stack2.pop()
    print(f"Popped item. Is it empty? {stack2.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
    queue1 = Queue()
    queue1.enqueue("Chelsea")
    queue1.enqueue("Monterrey")
    queue1.enqueue("Bayern")
    queue1.enqueue("Inter")



if __name__ == "__main__":
    main()
