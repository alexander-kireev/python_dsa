# implementing linked list

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value):

        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        
        self.length += 1
        return True


    def pop_last(self):
        curr = self.head
        prev = None

        if self.head == None:
            return None
        
        if self.head.next == None:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val

        while curr.next is not None:
            prev = curr
            curr = curr.next

        val = curr.value
        prev.next = None
        self.tail = prev
        self.length -= 1
        return val


    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


    def pop_first(self):

        if self.length == 0:
            return None
        
        val = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None
            
        else:
            self.head = self.head.next

        self.length -= 1
        return val


    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        
        counter = 0

        curr = self.head

        while counter < index:
            curr = curr.next
            counter += 1

        return curr


    def set(self, index, value):
        curr = self.get(index)

        if curr:
            curr.value = value
            return curr.value
    
        return None
        

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            curr = self.get(index - 1)

            if not curr:
                return None
            
            new_node = Node(value)
            new_node.next = curr.next
            curr.next = new_node
            self.length += 1
            return value


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        
        if index == self.length - 1:
            return self.pop_last()
        
        prev = self.get(index - 1)
        curr = prev.next

        prev.next = curr.next
        self.length -= 1
        return curr.value
    

    def reverse(self):
        if self.length < 2:
            return
        
        self.tail = self.head # ensure we have tail
        
        curr = self.head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev
        return True
            
    def partition_list_my_solution(self, value):

        left_head = None
        left_tail = None
        right_head = None
        right_tail = None

        curr = self.head
        
        while curr:
            
            if curr.value >= value:
                if not right_head:
                    right_head = curr
                    right_tail = curr
                    
                else:
                    right_tail.next = curr
                    right_tail = right_tail.next
                    right_tail.next = None
            else:
                if not left_head:
                    left_head = curr
                    left_tail = curr

                else:
                    left_tail.next = curr
                    left_tail = left_tail.next
                    left_tail.next = None

            
            curr = curr.next
            
        


        
        if left_head:
            left_tail.next = right_head
            
        else:
            self.head = right_head
        

        return self.head


    def partition_list_proper_solution(self, value):
        left_dummy = Node(0)
        right_dummy = Node(0)
        left_tail = left_dummy
        right_tail = right_dummy

        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = None

            if curr.value < value:
                left_tail.next = curr
                left_tail = left_tail.next
            else:
                right_tail.next = curr
                right_tail = right_tail.next

            curr = next_node

        
        left_tail.next = right_dummy.next
        self.head = left_dummy.next

        return self.head


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
# [1, 4, 3, 2, 5, 2, 5, 6, 7, 5, 8, 1, 9]
ll = LinkedList(1)
ll.append(4)
ll.append(3)
ll.append(2)
ll.append(5)
ll.append(2)
ll.append(5)
ll.append(6)
ll.append(7)
ll.append(5)
ll.append(8)
ll.append(1)
ll.append(9)


ll.partition_list(5)
ll.print_list()
