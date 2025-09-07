class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node 
    
    def search(self, key):
        return self._search(self.root,key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node 
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self._search(node.right, key)
        
    def inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)

    def delete(self,key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if not node:
            return node