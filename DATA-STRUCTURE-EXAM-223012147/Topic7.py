class Product:
    def __init__(self, product_name, price, priority):
        self.product_name = product_name
        self.price = price
        self.priority = priority

    def __repr__(self):
        return f"Product: {self.product_name}, Price: {self.price}, Priority: {self.priority}"

class Marketplace:
    products = []

    @classmethod
    def add_product(cls, product_name, price, priority):
        product = Product(product_name, price, priority)
        cls.products.append(product)
        print(f"Product '{product_name}' added successfully!")

    @classmethod
    def counting_sort(cls, place):
        size = len(cls.products)
        output = [None] * size
        count = [0] * 10

        for i in range(size):
            index = cls.products[i].priority // place
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = size - 1
        while i >= 0:
            index = cls.products[i].priority // place
            output[count[index % 10] - 1] = cls.products[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(size):
            cls.products[i] = output[i]

    @classmethod
    def radix_sort(cls):
        max_priority = max([product.priority for product in cls.products])
        place = 1
        while max_priority // place > 0:
            cls.counting_sort(place)
            place *= 10

    @classmethod
    def display_products(cls):
        if cls.products:
            print("\nSorted products based on priority:")
            for product in cls.products:
                print(product)
        else:
            print("No products available to display.")


# Execution
Marketplace.add_product("hp ltebook 1030 g2", "500,000 RWF", 2)
Marketplace.add_product("Lenovo i7", "400,000 RWF", 5)
Marketplace.add_product("play station ps", "100,000 RWF", 3)
Marketplace.add_product("hp ltebook 1030 g1", "500,000 RWF", 1)

print("Before sorting:")
Marketplace.display_products()
Marketplace.add_product("Dell XPS 13", "800,000 RWF", 4)
Marketplace.add_product("MacBook Pro", "1,200,000 RWF", 6)
Marketplace.radix_sort()

print("\nAfter sorting:")
Marketplace.display_products()
