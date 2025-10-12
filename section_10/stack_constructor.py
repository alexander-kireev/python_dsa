class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.height = 1



    def print_stack(self):
        cur = self.top

        while cur:
            print(cur.value)
            cur = cur.next


    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
        self.height += 1

        return self.top
    

    def pop(self):
        if not self.top:
            return None

        cur = self.top.next
        self.top.next = None
        self.top = cur
        self.height -= 1

        return self.top


s = Stack(5)
s.push(9)
s.push(75)
s.pop()
s.pop()
s.print_stack()