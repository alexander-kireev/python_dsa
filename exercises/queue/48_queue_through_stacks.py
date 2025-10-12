

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.length = 0
        self.first = None

    
    def peek(self):
        if self.stack1 is not None:
            return self.stack1[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.stack1) == 0
    

    def enqueue(self, value):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(value)

        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())

        self.length += 1

        self.first = self.stack1[-1]


    def dequeue(self):
        popped = None
        if not self.is_empty():
            self.length -= 1
            popped = self.stack1.pop()
        
        return popped
        
    
    def print_queue(self):
        counter = 0

        for i in range(self.length-1, -1, -1):
            print(f"position {counter} : {self.stack1[i]}")
            counter += 1




my_queue = Queue()

my_queue.enqueue(5)
my_queue.enqueue(10)
my_queue.enqueue(15)
my_queue.enqueue(20)

my_queue.print_queue()