# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
    While completing this assignment I learnt how to implement a binary search tree (BST) from scratch using
    recursive methods to insert, search and order the tree. I learned more about tree structures like how
    they maintain relationships to other nodes
2. What challenges did you encounter, and how did you overcome them?
    The main challenge were definitely the recursive return references in the search and in-order methods.
    I overcame this issue by using breakpoints to follow the flow of the program and paying close attention 
    on how the references were updated.
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
    Compared to other data structures like lists, stacks or queues, a binary search tree seems like a more efficient 
    data structure. In a sorted array, searching takes O(log n) time using binary search, but inserting or deleting 
    elements requires shifting elements in memory, taking O(n) time. In contrast, a BST provides efficient dynamic 
    performance on average, dividing the search space in half with every comparison by routing values either left or
    right based on whether they are smaller or larger than the current node.