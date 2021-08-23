class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root:
            x = self.root
            while True:
                if x.value > new_val:
                    if x.left:
                        x = x.left
                    else:
                        x.left = Node(new_val)
                        break
                elif x.value < new_val:
                    if x.right:
                        x = x.right
                    else:
                        x.right = Node(new_val)
                        break
        else:
            self.root = new_val


    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        if not isinstance(find_val, int):
            return False
        x = self.root
        while x != None:
            if x.value == find_val:
                return True
            elif x.value > find_val:
                x = x.left
            elif x.value < find_val:
                x = x.right
        return False
