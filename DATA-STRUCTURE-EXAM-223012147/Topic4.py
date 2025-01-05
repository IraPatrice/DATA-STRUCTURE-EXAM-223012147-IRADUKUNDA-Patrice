class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def enqueue(self, order):
        if self.size == self.capacity:
            print("Cannot add order. The order queue is full!")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = order
        self.size += 1
        print(f"Order added: {order}")

    def dequeue(self):
        if self.size == 0:
            print("Cannot process order. The order queue is empty!")
            return

        order = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Order processed: {order}")

    def display_orders(self):
        if self.size == 0:
            print("There are no orders to display!")
            return

        print("\nHere are the current orders in the queue:")
        index = self.front
        for _ in range(self.size):
            print(self.queue[index])
            index = (index + 1) % self.capacity
        print("--------------------------------")


# Execution
order_circular_queue = CircularQueue(3)

order_circular_queue.enqueue({"product": "Laptop", "quantity": "1", "Amount": "700,000 RWF"})
order_circular_queue.enqueue({"product": "Table", "quantity": "2", "Amount": "240,000 RWF"})
order_circular_queue.enqueue({"product": "Chair", "quantity": "4", "Amount": "200,000 RWF"})
order_circular_queue.display_orders()

order_circular_queue.enqueue({"product": "Bookshelf", "quantity": "1", "Amount": "250,000 RWF"})

order_circular_queue.dequeue()
order_circular_queue.display_orders()

order_circular_queue.enqueue({"product": "Bookshelf", "quantity": "1", "Amount": "250,000 RWF"})
order_circular_queue.display_orders()
