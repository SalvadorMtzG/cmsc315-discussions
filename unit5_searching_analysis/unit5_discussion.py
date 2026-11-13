"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for i in lst:
        if i == target:
            return lst.index(i)

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) -1
    while low <= high:
        mid = int((low + high)/2)
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    print(f"List: {list}")
    print(f"Linear search for '40' returned: {linear_search(list, 40)}")
    print(f"Linear search for '100' returned: {linear_search(list, 100)}")
    print(f"Binary search for '60' returned: {binary_search(list, 60)}")
    print(f"Binary search for '600' returned: {binary_search(list, 600)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")
    array = []
    for i in range(100):
        array.append(i)
    print(f"Linear search for '2' returned: {linear_search(array, 2)}")
    print(f"Linear search for '68' returned: {linear_search(array, 68)}")
    print(f"Binary search for '150' returned: {binary_search(array, 150)}")
    print(f"Binary search for '600' returned: {binary_search(array, 600)}")
    print()
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    empty = []
    singleElement = [1000]

    print(f"Searching value in empty list: {binary_search(empty, 50)}")
    print(f"Searching value in single element list: {binary_search(singleElement, 1000)}")
    print(f"Searching value in not present in single element list: {binary_search(singleElement, 100)}")


if __name__ == "__main__":
    main()