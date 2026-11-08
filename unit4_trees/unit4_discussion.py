"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""
from logging import root
from signal import valid_signals


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The new value is compared with the current value
        # If the value is smaller, it goes to the left subtree
        # If the value is larger, it goes to the right subtree
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # If we reach an empty, we create and return the new node
        if node is None:
            return Node(value)

        # Recursive step, we decide if we go left or right
        if value < node.value:
            node.leftChild = self._insert_recursive(node.leftChild, value)
        elif value > node.value:
            node.rightChild = self._insert_recursive(node.rightChild, value)

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        #BST is more effective because at each level we drop half of the search space by comparing the value
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Return False if the node is None or True if it matches the value
        if node is None:
            return False
        elif node.value == value:
            return True

        # Recursive step, we decide if we go left or right
        if value < node.value:
            return self._search_recursive(node.leftChild, value)
        else:
            return self._search_recursive(node.rightChild, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        ids = []
        self._inorder_recursive(self.root, ids)
        return ids

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        #It produces sorted output because we visit left subtrees (smaller values) first

        if node is not None:
            # Visiting left subtree
            self._inorder_recursive(node.leftChild, values)
            # Visiting current node
            values.append(node.value)
            # Visiting right subtree
            self._inorder_recursive(node.rightChild, values)

    def preorder(self):
        ids = []
        self._preorder_recursive(self.root, ids)
        return ids

    def _preorder_recursive(self, node, values):
        if node is not None:
            values.append(node.value)
            self._preorder_recursive(node.leftChild, values)
            self._preorder_recursive(node.rightChild, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("Employee ID system")
    id_tree = BST()

    employee_ids = [50, 30, 70, 40, 10, 80, 60]
    for id in employee_ids:
        id_tree.insert(id)
        print(f"Inserted employee with ID: {id}")


    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")
    print(f"Preorder traversal results: {id_tree.preorder()}")
    print(f"In-order traversal results: {id_tree.inorder()}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    print(f"Search for '50' (Exists): {id_tree.search(50)}")
    print(f"Search for '80' (Exists): {id_tree.search(80)}")
    print(f"Search for '5' (Doesn't exist): {id_tree.search(5)}")
    print(f"Search for '95' (Doesn't exist): {id_tree.search(95)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")
    empty_tree = BST()
    print(f"Traversing an empty tree: {empty_tree.inorder()}")
    print(f"Searching in an empty tree: {empty_tree.search(10)}")



if __name__ == "__main__":
    main()