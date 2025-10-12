class Stack:
    def __init__(self, value=None):
        self.values = []
        if value:
            self.values.append(value)
        
        self.height = len(self.values)

        if self.values:
            self.top = self.values[-1]
        else:
            self.top = None

    
    def print_stack(self):

        for i in range(self.height-1, -1, -1):
            print(self.values[i])


    def push(self, value):
        self.values.append(value)
        self.height += 1
        self.top = self.values[self.height - 1]
        return value


    def pop(self):
        if self.height == 0:
            return None

        first = self.top
        self.values.pop()
        self.height -= 1

        if self.height == 0:
            self.top = None
        else:
            self.top = self.values[self.height - 1]
        
        return first


    def is_empty(self):
        return self.height == 0
    

    def peek(self):
        return self.top

        


def stack_sort(og_stack):
    s1 = og_stack
    s2 = Stack()

    while not s1.is_empty():

        temp = s1.pop()

        while not s2.is_empty() and s2.peek() > temp:
            s1.push(s2.pop())

        s2.push(temp)


    while not s2.is_empty():
        s1.push(s2.pop())


    return s1







stack = Stack()

my_list = [2, 4, 1, 1, 3, 1, 3, 4, 1, 2, 3]


for i in my_list:
    stack.push(i)


s1 = stack_sort(stack)

s1.print_stack()