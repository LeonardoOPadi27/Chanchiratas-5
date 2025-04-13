# Complete implementation of a Singly Linked List (SLL)

class Node:
    """Class representing a node in the linked list"""
    def __init__(self, data=None): #Node's Constructor
        self.data = data
        self.next = None
    
    def getData(self): #Get data of the node
        return self.data
    
    def setData(self, data): #Define the data value
        self.data = data
    
    def getNext(self): #Get the next node
        return self.next
    
    def setNext(self, next_node): #Set the next node's data
        self.next = next_node

class LinkedList:
    """Class implementing a singly linked list"""
    def __init__(self): #Linked list's constructor
        self.head = None
        self.length = 0
    
    def listLength(self): #Get the length of the linked list (LL)
        """Traverses the list and counts the number of nodes"""
        current = self.head #The initial value is the head's data
        count = 0 #
        
        while current != None:
            count = count + 1
            current = current.getNext()
        
        return count
    
    def insertAtBeginning(self, data):
        """Inserts a new node at the beginning of the list"""
        newNode = Node(data)
        
        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode
        
        self.length += 1
        return True
    
    def insertAtEnd(self, data):
        """Inserts a new node at the end of the list"""
        newNode = Node(data)
        
        if self.length == 0:
            self.head = newNode
            self.length += 1
            return True
            
        current = self.head
        
        while current.getNext() != None:
            current = current.getNext()
        
        current.setNext(newNode)
        self.length += 1
        return True
    
    def insertAtPos(self, pos, data):
        """Inserts a new node at the specified position"""
        if pos > self.length or pos < 0:
            return False
        
        if pos == 0:
            return self.insertAtBeginning(data)
        
        if pos == self.length:
            return self.insertAtEnd(data)
        
        newNode = Node(data)
        count = 0
        current = self.head
        
        while count < pos - 1:
            count += 1
            current = current.getNext()
        
        newNode.setNext(current.getNext())
        current.setNext(newNode)
        self.length += 1
        return True
    
    def deleteFromBeginning(self):
        """Deletes the first node from the list"""
        if self.length == 0:
            return None
        
        temp = self.head
        data = temp.getData()
        self.head = temp.getNext()
        temp = None
        self.length -= 1
        return data
    
    def deleteFromEnd(self):
        """Deletes the last node from the list"""
        if self.length == 0:
            return None
        
        if self.length == 1:
            data = self.head.getData()
            self.head = None
            self.length = 0
            return data
        
        current = self.head
        
        # Traverse to the second-to-last node
        while current.getNext().getNext() != None:
            current = current.getNext()
        
        data = current.getNext().getData()
        current.setNext(None)
        self.length -= 1
        return data
    
    def deleteFromPos(self, pos):
        """Deletes a node from the specified position"""
        if pos >= self.length or pos < 0:
            return None
        
        if pos == 0:
            return self.deleteFromBeginning()
        
        if pos == self.length - 1:
            return self.deleteFromEnd()
        
        count = 0
        current = self.head
        
        while count < pos - 1:
            count += 1
            current = current.getNext()
        
        temp = current.getNext()
        data = temp.getData()
        current.setNext(temp.getNext())
        temp = None
        self.length -= 1
        return data
    
    def clear(self):
        """Removes all nodes from the list"""
        self.head = None
        self.length = 0
        return True
    
    def search(self, data):
        """Searches for a value in the list and returns its position or -1 if not found"""
        if self.length == 0:
            return -1
        
        current = self.head
        position = 0
        
        while current != None:
            if current.getData() == data:
                return position
            current = current.getNext()
            position += 1
        
        return -1
    
    def getNthFromEnd(self, n):
        """Finds the nth node from the end of the list"""
        if n <= 0 or n > self.length:
            return None
        
        # The nth from the end is the (length-n+1)th from the beginning
        pos = self.length - n
        
        current = self.head
        count = 0
        
        while count < pos:
            current = current.getNext()
            count += 1
        
        return current.getData()
    
    def display(self):
        """Displays all elements in the list"""
        if self.length == 0:
            return "Empty list"
        
        result = ""
        current = self.head
        
        while current != None:
            result += str(current.getData()) + " -> "
            current = current.getNext()
        
        return result + "None"

# Test cases
def test_cases():
    print("===== SINGLY LINKED LIST TESTS =====\n")
    
    # Create an empty linked list
    print("Creating linked list...")
    my_list = LinkedList()
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Insert at the beginning
    print("Inserting elements at the beginning...")
    my_list.insertAtBeginning(5)
    my_list.insertAtBeginning(10)
    my_list.insertAtBeginning(15)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Insert at the end
    print("Inserting elements at the end...")
    my_list.insertAtEnd(20)
    my_list.insertAtEnd(25)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Insert at specific position
    print("Inserting elements at specific positions...")
    my_list.insertAtPos(2, 30)
    my_list.insertAtPos(4, 35)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Search for elements
    print("Searching for elements...")
    print(f"Position of 30: {my_list.search(30)}")
    print(f"Position of 100: {my_list.search(100)}\n")
    
    # Find nth element from the end
    print("Finding elements from the end...")
    print(f"2nd element from the end: {my_list.getNthFromEnd(2)}")
    print(f"4th element from the end: {my_list.getNthFromEnd(4)}\n")
    
    # Delete from the beginning
    print("Deleting elements from the beginning...")
    deleted = my_list.deleteFromBeginning()
    print(f"Deleted element: {deleted}")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Delete from the end
    print("Deleting elements from the end...")
    deleted = my_list.deleteFromEnd()
    print(f"Deleted element: {deleted}")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Delete from specific position
    print("Deleting elements from specific positions...")
    deleted = my_list.deleteFromPos(2)
    print(f"Element deleted from position 2: {deleted}")
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")
    
    # Clear the list
    print("Clearing the list...")
    my_list.clear()
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")

    # Verify operations after clearing
    print("Inserting new elements after clearing...")
    my_list.insertAtBeginning(100)
    my_list.insertAtEnd(200)
    my_list.insertAtPos(1, 150)
    print(f"List: {my_list.display()}")
    print(f"Length: {my_list.listLength()}\n")

if __name__ == "__main__":
    test_cases()