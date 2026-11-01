"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""
from enum import nonmember

lst = [0,1,2,3,4,5]

def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Inserting an element at the beginning or middle of a list causes all elements to the right to shift (O(n))
    # Inserting an element at the end does not affect the elements in the list (O(1)
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    #Index validation and safe deletion are important to avoid exceptions and program crashes
    if index >= len(lst) or index < 0:
        print("Invalid index")
        return None
    else:
        print(f"Item {index} removed")
        return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    #This is a linear search because it checks elemnts one by one until the value is found or the whole list is checked
    i = 0
    while i < len(lst):
        if lst[i] == value:
            return i
        i+=1
    print("Value not found")
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.
    list1 = [1,2,3,4,5]
    print(f"Original list: {list1}")
    insert_at(list1, 0, 10)
    print(f"'10' inserted at the beginning: {list1}")
    insert_at(list1, 2, 9)
    print(f"'9' inserted in the middle: {list1}")
    insert_at(list1, len(list1), 8)
    print(f"'8' inserted at the end: {list1}")


    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    print(f"Original list: {list1}")
    delete_at(list1, 0)
    print(f"Deleted from beginning: {list1}")
    delete_at(list1, 1)
    print(f"Deleted from the middle: {list1}")
    delete_at(list1, len(list1) - 1)
    print(f"Deleted from end: {list1}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    print(f"Original list: {list1}")
    print(f"Searching '1', is in index: {search_value(list1, 1)}")
    print(f"Searching '10', is in index: {search_value(list1, 10)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    print(f"Original list: {list1}")
    #Deleting an invalid index
    delete_at(list1, 10)
    #Searching a missing value
    search_value(list1, 10)



if __name__ == "__main__":
    main()