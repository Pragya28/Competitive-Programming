"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        if self.head == None:
            self.head = new_element
        else:
            x = self.head
            while x.next != None:
                x = x.next
            x.next = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if self.head == None:
            return None
        i = 1
        x = self.head
        while x != None and i < position:
            x = x.next
            i += 1
        return x
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            ele = new_element
            ele.next = self.head
            self.head = ele
        i = 1
        x = self.head
        y = None
        while x != None and i < position:
            y = x
            x = x.next
            i += 1
        # y = x.next
        y.next = new_element
        y = y.next
        y.next = x
    
    def delete(self, value):
        """Delete the first node with a given value."""
        if self.head.value == value:
            self.head = self.head.next
            return self.head
        x = self.head
        y = None
        while x != None:
            if x.value == value:
                break
            y = x
            x = x.next
        if x != None:
            y.next = x.next
        return y
