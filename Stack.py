class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f'Popped: {removed}')
            return removed
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            print(f'Top element: {self.stack[-1]}')
            return self.stack[-1]
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        print(f'Size of the stack: {len(self.stack)}')
        return len(self.stack)
    

s = Stack()
s.push(10)
s.push(20)
s.peek()
s.pop()
s.size()
s.pop()
s.pop()