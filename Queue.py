class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty. Cannot dequeue.")

    def size(self):
        return len(self.items)

my_queue = Queue()

print("Is the queue empty?", my_queue.is_empty())  

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

print("Is the queue empty?", my_queue.is_empty())  
print("Queue size:", my_queue.size())              

print("Dequeue:", my_queue.dequeue())             
print("Queue size:", my_queue.size())             
