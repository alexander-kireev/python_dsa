class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    


class BST:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return value
        
        cur = self.root
        prev = None

        while cur is not None:
            prev = cur

            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        if value < prev.value:
            prev.left = new_node
        else:
            prev.right = new_node
        
        return value


    def contains(self, value):
        
        cur = self.root

        while cur:

            if cur.value == value:
                return True
            
            if value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        
        return False