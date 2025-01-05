from collections import deque

class MarketplaceQueue:
    def __init__(self):
        self.products_queue = deque()

    def add_product(self, product):
        self.products_queue.append(product)
        print(f"Product added to queue: {product}")

    def process_product(self):
        if self.products_queue:
            product = self.products_queue.popleft()
            print(f"Product processed from queue: {product}")
        else:
            print("No products in queue to process!")

    def display_products(self):
        if self.products_queue:
            print("\nProducts in Queue:")
            for product in self.products_queue:
                print(product)
            print("--------------------------------")
        else:
            print("There are no products in the queue!")

# Execution
marketplace_queue = MarketplaceQueue()

marketplace_queue.add_product({"productName": "Handmade Necklace", "price": "50,000 RWF"})
marketplace_queue.add_product({"productName": "Wooden Chair", "price": "120,000 RWF"})
marketplace_queue.add_product({"productName": "Clay Pot", "price": "15,000 RWF"})
marketplace_queue.display_products()
marketplace_queue.process_product()
marketplace_queue.display_products()

