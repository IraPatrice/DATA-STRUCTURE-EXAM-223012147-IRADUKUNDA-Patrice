
#Implemention of Deque and Queue to manage data in the online marketplace for handmade goods.
from collections import deque

class FeaturedProducts:
    def __init__(self):
        self.productsDeque = deque()

    def add_product_front(self, product):
        self.productsDeque.appendleft(product)
        print(f"Product added to front: {product}")

    def add_product_back(self, product):
        self.productsDeque.append(product) 
        print(f"Product added to back: {product}")

    def remove_product_front(self):
        if self.productsDeque:
            product = self.productsDeque.popleft()
            print(f"Product removed from front: {product}")
        else:
            print("No products to remove from front!")

    def remove_product_back(self):
        if self.productsDeque:
            product = self.productsDeque.pop()  
            print(f"Product removed from back: {product}")
        else:
            print("No products to remove from back!")
    def display_products(self):
        if self.productsDeque:
            print("\nHere are available products:")
            for order in self.productsDeque:
                print(order)
            print("--------------------------------")
            
        else:
            print("There is no product featured yet!")
    
class OrderQueue:
    
    def __init__(self):
        self.orders = deque()

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order Setted: {order}")

    def process_order(self):
        if self.orders:
            order = self.orders.popleft()
            print(f"Order Served: {order}")
        else:
            print("No orders to process!")
    
    def display_orders(self):
        if self.orders:
            print("\nHere are available orders:")
            for order in self.orders:
                print(order)
            print("--------------------------------")
            
        else:
            print("There is no orders setted yet!")
    


#execution
featured_products = FeaturedProducts()
featured_products.add_product_front({"productName":"hp ltebook 1030 g2","price":"500,000 rwf"})
featured_products.add_product_back({"productName":"hp ltebook 1030 g1","price":"500,000 rwf"})
featured_products.add_product_back({"productName":"Lenovo i7","price":"400,000 rwf"})
featured_products.add_product_front({"productName":"play station ps","price":"100,000 rwf"})
featured_products.display_products()
featured_products.remove_product_front()
featured_products.display_products()
featured_products.remove_product_back()
featured_products.display_products()


order_queue = OrderQueue()
order_queue.add_order({"product":"Lenovo i7","quantity":"2","Amount":"800,000,000 rwf"})
order_queue.add_order({"product":"hp ltebook 1030 g1","quantity":"1","Amount":"500,000 rwf"})
order_queue.display_orders()
order_queue.process_order()
order_queue.display_orders()




