class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f'Enqueued {item}')

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f'Dequeued: {removed}')
            return removed
        else:
            print("Queue is empty. Cannot dequeue.")

    def peek(self):
        if not self.is_empty():
            print(f'Front element: {self.queue[0]}')
            return self.queue[0]
        else:
            print('Queue is empty.')

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        print(f'Size of queue: {len(self.queue)}')
        return len(self.queue)
    

q = Queue()
q.enqueue(100)
q.enqueue(200)
q.peek()
q.dequeue()
q.size()
q.dequeue()
q.dequeue()