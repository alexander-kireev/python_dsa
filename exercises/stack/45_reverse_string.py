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


    def reverse_string(self, string):
        
        reversed_chars = []
        for char in string:
            self.push(char)

        for _ in range(len(string)):
            popped_char = self.pop()
            reversed_chars.append(popped_char)

        return ''.join(reversed_chars)

word = "hello"

stack = Stack()

print(stack.reverse_string(word))