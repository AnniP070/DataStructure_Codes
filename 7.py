class TreeNode: 
    """Class representing a node in a binary search tree.""" 
    def __init__(self, key): 
        self.key = key 
        self.left = None 
        self.right = None 

 
class BinarySearchTree: 
    def __init__(self): 
        self.root = None 
 
    # a) Insert (handle duplicate entries) 
    def insert(self, key): 
        self.root = self._insert(self.root, key) 
 
    def _insert(self, node, key): 
        if node is None: 
            return TreeNode(key) 
        elif key < node.key: 
            node.left = self._insert(node.left, key) 
        elif key > node.key: 
            node.right = self._insert(node.right, key) 
        else: 
            print(f"Duplicate entry '{key}' not inserted.") 
        return node 
 
    # b) Delete a node 
    def delete(self, key): 
        self.root = self._delete(self.root, key) 
 
    def _delete(self, node, key): 
        if node is None: 
            return None 
        if key < node.key: 
            node.left = self._delete(node.left, key) 
        elif key > node.key: 
            node.right = self._delete(node.right, key) 
        else: 
            # Node with only one child or no child 
            if node.left is None: 
                return node.right 
            elif node.right is None: 
                return node.left 
            # Node with two children: Get the inorder successor (smallest in the right subtree) 
            min_larger_node = self._find_min(node.right) 
            node.key = min_larger_node.key 
            node.right = self._delete(node.right, min_larger_node.key) 
        return node 
 
    def _find_min(self, node): 
        while node.left is not None: 
            node = node.left 
        return node 
 
    # c) Search for a key 
    def search(self, key): 
        return self._search(self.root, key) 
 
    def _search(self, node, key): 
        if node is None or node.key == key: 
            return node 
        if key < node.key: 
            return self._search(node.left, key) 
        return self._search(node.right, key) 
 
    # d) Display tree (In-order Traversal) 
    def inorder(self): 
        self._inorder(self.root) 
        print() 
 
    def _inorder(self, node): 
        if node: 
            self._inorder(node.left) 
            print(node.key, end=' ') 
            self._inorder(node.right) 
 
    # e) Depth of the tree 
    def depth(self): 
        return self._depth(self.root) 
 
    def _depth(self, node): 
        if node is None: 
            return 0 
        return 1 + max(self._depth(node.left), self._depth(node.right)) 
 
    # f) Mirror image of the tree 
    def mirror(self): 
        self._mirror(self.root) 
 
    def _mirror(self, node): 
        if node: 
            node.left, node.right = node.right, node.left 
            self._mirror(node.left) 
            self._mirror(node.right) 
 
    # g) Create a copy of the tree 
    def copy(self): 
        return self._copy(self.root) 
 
    def _copy(self, node): 
        if node is None: 
            return None 
        new_node = TreeNode(node.key) 
        new_node.left = self._copy(node.left) 
        new_node.right = self._copy(node.right) 
        return new_node 
 
    # h) Display all parent nodes with their child nodes 
    def display_parents(self): 
        self._display_parents(self.root) 
 
    def _display_parents(self, node): 
        if node: 
            print(f"Node {node.key}: Left -> {node.left.key if node.left else None}, Right -> {node.right.key if node.right else None}") 
            self._display_parents(node.left) 
            self._display_parents(node.right) 
 
    # i) Display leaf nodes 
    def display_leaves(self): 
        self._display_leaves(self.root) 
        print() 
 
    def _display_leaves(self, node): 
        if node: 
            if node.left is None and node.right is None: 
                print(node.key, end=' ') 
            self._display_leaves(node.left) 
            self._display_leaves(node.right) 
 
    # j) Display tree level-wise 
    def level_order(self): 
        if self.root is None: 
            return 
        queue = [self.root] 
        while queue: 
            current = queue.pop(0) 
            print(current.key, end=' ') 
            if current.left: 
                queue.append(current.left) 
            if current.right: 
                queue.append(current.right) 
        print() 
 
 
# Example usage of the Binary Search Tree 
if __name__ == "__main__": 
    bst = BinarySearchTree() 
 
    # Insert nodes into the BST 
    keys = [50, 30, 70, 20, 40, 60, 80, 70]  # Including a duplicate entry (70) 
    for key in keys: 
        bst.insert(key) 
 
    print("In-order Traversal:") 
    bst.inorder() 
 
    print("Tree Depth:", bst.depth()) 
 
    print("\nLevel Order Traversal:") 
    bst.level_order() 
 
    print("\nDisplaying Parent Nodes:") 
    bst.display_parents() 
 
    print("\nLeaf Nodes:") 
    bst.display_leaves() 
 
    print("\nSearching for 40:", "Found" if bst.search(40) else "Not Found") 
    print("Searching for 100:", "Found" if bst.search(100) else "Not Found") 
 
    print("\nDeleting Node 20") 
    bst.delete(20) 
    bst.inorder() 
 
    print("\nMirror Image of Tree:") 
    bst.mirror() 
    bst.inorder() 
 
    print("\nCopying Tree:") 
    bst_copy = bst.copy() 
    print("In-order Traversal of Copied Tree:") 
    bst_copy_tree = BinarySearchTree() 
    bst_copy_tree.root = bst_copy 
    bst_copy_tree.inorder()