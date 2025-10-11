class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None




class DLL:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head

        while temp:
            print(temp.value)
            temp = temp.next


    def append(self, value):

        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node 
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True
        

    def pop(self):
        
        if self.length == 0:
            return None
        
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return temp


    def prepend(self, value):

        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True


    def pop_first(self):

        if self.length == 0:
            return None
        
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        
        self.length -= 1

        return temp
    
    
    def get(self, index):

        if index < 0 or index >= self.length:
            return None
        
        if index < self.length // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.length - index - 1):
                cur = cur.prev

        return cur


    def set(self, index, value):
        if cur := self.get(index):
            cur.value = value
            return True
        else:
            return False


    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        elif cur := self.get(index - 1):
            new_node = Node(value)
            next_node = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = next_node
            next_node.prev = new_node
            self.length += 1
            return True
        
        return False
    

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif cur := self.get(index):
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            self.length -= 1
            return cur
        return False
    
    def is_pallindrome(self):
        # set both cursors to head
        left = self.head
        right = self.head

        # if list is empty
        if not left:
            return True

        # traverse list, finding the tail
        while right.next:
            right = right.next
        
        # traverse list from both ends to middle
        while left != right and left.prev != right:
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev

        return True
    
dll = DLL(1)
dll.append(2)
dll.append(1)

print(dll.is_pallindrome())