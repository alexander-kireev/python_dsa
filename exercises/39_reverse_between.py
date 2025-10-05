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
            

    def reverse_between(self, start, end):

        # get head of ll, set a counter and establish a tracking var
        node_before_reverse = self.head
        counter = 0
        tracker = None

        # get the node before the first node that needs to be reversed
        while counter < start - 1:

            # ensure node exists
            if not node_before_reverse:
                return None
            
            # select next node and increment counter
            node_before_reverse = node_before_reverse.next
            counter += 1

        # get the first node that is supposed to be reversed
        curr = node_before_reverse.next

        # save a copy of this node for later. later, this node will
        # need to be attached to the 'end' node, which is the node
        # that DOES NOT NEED TO BE REVERSED after the reversed nodes
        to_be_reattached = curr

        # reverse nodes
        while counter < end:

            # save a copy of the next node
            next_node = curr.next

            # get current node's pointer and prepend it to tracker var
            curr.next = tracker

            # update tracker to the current node
            tracker = curr

            # switch to next node for next iteration of loop, increment counter
            curr = next_node
            counter += 1
        
        # if the reversal started from the previous head
        if start == 0:

            # set head to the last node that was reversed
            self.head = tracker        
        
        else:
            node_before_reverse.next = tracker
            
        to_be_reattached.next = next_node
        return self.head
# TODO: 2 BUGS - OUT OF RANGE (1, 5) AND START FROM 0 (0,3)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.reverse_between(1, 5)
ll.print_list()
