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

        

