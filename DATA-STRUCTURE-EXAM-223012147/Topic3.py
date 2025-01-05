class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _get_balance(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))
        return y

    def _insert(self, node, key, value):
        if not node:
            return Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            return node

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def add_product(self, key, value):
        print(f"Adding product with ID {key}: {value}")
        self.root = self._insert(self.root, key, value)

    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.value = temp.value
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def remove_product(self, key):
        print(f"Removing product with ID {key}")
        self.root = self._delete(self.root, key)

    def _in_order_traversal(self, node):
        if node:
            self._in_order_traversal(node.left)
            print(f"Product ID: {node.key}, Details: {node.value}")
            self._in_order_traversal(node.right)

    def display_products(self):
        print("\nAvailable Products (In-order Traversal):")
        if self.root:
            self._in_order_traversal(self.root)
        else:
            print("No products available yet!")

products_avl = AVLTree()
products_avl.add_product(101, {"productName": "Laptop", "price": "700,000 RWF"})
products_avl.add_product(102, {"productName": "Table", "price": "120,000 RWF"})
products_avl.add_product(100, {"productName": "Chair", "price": "50,000 RWF"})
products_avl.add_product(103, {"productName": "Bookshelf", "price": "250,000 RWF"})
products_avl.display_products()
products_avl.remove_product(102)
products_avl.display_products()
