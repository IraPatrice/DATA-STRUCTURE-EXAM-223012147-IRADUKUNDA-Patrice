class ProductNode:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        self.right = None

class CategoryNode:
    def __init__(self, category_name):
        self.category_name = category_name
        self.products = None
        self.left = None
        self.right = None

    def add_product(self, product_name, price):
        new_product = ProductNode(product_name, price)
        if not self.products:
            self.products = new_product
        else:
            current_product = self.products
            while current_product.right:
                current_product = current_product.right
            current_product.right = new_product

class MarketplaceTree:
    def __init__(self):
        self.root = None

    def _insert_category(self, node, category_name):
        if not node:
            return CategoryNode(category_name)
        if category_name < node.category_name:
            node.left = self._insert_category(node.left, category_name)
        elif category_name > node.category_name:
            node.right = self._insert_category(node.right, category_name)
        return node

    def add_category(self, category_name):
        if not self.root:
            self.root = CategoryNode(category_name)
        else:
            self._insert_category(self.root, category_name)

    def _find_category(self, node, category_name):
        if node:
            if node.category_name == category_name:
                return node
            elif category_name < node.category_name:
                return self._find_category(node.left, category_name)
            elif category_name > node.category_name:
                return self._find_category(node.right, category_name)
        return None

    def add_product(self, category_name, product_name, price):
        category = self._find_category(self.root, category_name)
        if category:
            category.add_product(product_name, price)
        else:
            print(f"Category '{category_name}' not found!")

    def _in_order_traversal(self, node, level=0):
        if node:
            self._in_order_traversal(node.left, level + 1)
            print(f"{' ' * level * 4}Category: {node.category_name}")
            if node.products:
                current_product = node.products
                while current_product:
                    print(f"{' ' * (level + 1) * 4}Product: {current_product.product_name}, Price: {current_product.price}")
                    current_product = current_product.right
            self._in_order_traversal(node.right, level + 1)

    def display_products(self):
        print("\nDisplaying products in the marketplace as a hierarchical tree:")
        if self.root:
            self._in_order_traversal(self.root)
        else:
            print("No products available!")

# Execution
marketplace_tree = MarketplaceTree()
marketplace_tree.add_category("Electronics")
marketplace_tree.add_category("Furniture")
marketplace_tree.add_category("Clothing")

marketplace_tree.add_product("Electronics", "iPhone 13", "1,200,000 RWF")
marketplace_tree.add_product("Electronics", "Samsung Galaxy S21", "1,000,000 RWF")
marketplace_tree.add_product("Furniture", "Wooden Table", "150,000 RWF")
marketplace_tree.add_product("Furniture", "Office Chair", "80,000 RWF")
marketplace_tree.add_product("Clothing", "Cotton Shirt", "20,000 RWF")
marketplace_tree.add_product("Clothing", "Denim Pants", "30,000 RWF")

marketplace_tree.display_products()
