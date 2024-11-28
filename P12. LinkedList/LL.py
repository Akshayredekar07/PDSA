class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Link the new node

    def delete_node(self, key):
        """Delete the first occurrence of a node with the given key."""
        current_node = self.head
        
        # If head node itself holds the key to be deleted
        if current_node and current_node.data == key:
            self.head = current_node.next  # Change head
            current_node = None  # Free memory
            return
        
        # Search for the key to be deleted, keep track of the previous node
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next
        
        # If key was not present in linked list
        if not current_node:
            return
        
        # Unlink the node from linked list
        prev_node.next = current_node.next
        current_node = None  # Free memory

    def traverse(self):
        """Print all elements in the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # Indicate end of list

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    
    print("Linked List after insertion:")
    sll.traverse()  # Output: 10 -> 20 -> 30 -> None

    sll.delete_node(20)
    
    print("Linked List after deletion:")
    sll.traverse()  # Output: 10 -> 30 -> None        