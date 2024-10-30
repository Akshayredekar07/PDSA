
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def sortedInsert(self, head, x):
        # Create new node to insert
        toInsert = Node(x)
        
        # Case 1: Insert at beginning
        if x <= head.data:
            toInsert.next = head
            head.prev = toInsert
            return toInsert
        
        # Case 2: Insert in middle or end
        curr = head.next
        prev = head
        
        while curr is not None and x > curr.data:
            prev = curr
            curr = curr.next
        
        # Insert between prev and curr
        prev.next = toInsert
        toInsert.prev = prev
        
        # If not inserting at end
        if curr is not None:
            curr.prev = toInsert
            toInsert.next = curr
            
        return head
    
    def printList(self, head):
        """Utility function to print the doubly linked list"""
        current = head
        print("Forward Traversal:", end=" ")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def createList(self, arr):
        """Utility function to create a new doubly linked list from array"""
        if not arr:
            return None
        
        head = Node(arr[0])
        current = head
        
        for i in range(1, len(arr)):
            newNode = Node(arr[i])
            current.next = newNode
            newNode.prev = current
            current = newNode
            
        return head

def main():
    solution = Solution()
    
    # Test Case 1: Insert in middle
    print("Test Case 1: Insert 4 in [1, 3, 5]")
    head1 = solution.createList([1, 3, 5])
    print("Before insertion:")
    solution.printList(head1)
    head1 = solution.sortedInsert(head1, 4)
    print("After insertion:")
    solution.printList(head1)
    print()
    
    # Test Case 2: Insert at beginning
    print("Test Case 2: Insert 0 in [1, 2, 3]")
    head2 = solution.createList([1, 2, 3])
    print("Before insertion:")
    solution.printList(head2)
    head2 = solution.sortedInsert(head2, 0)
    print("After insertion:")
    solution.printList(head2)
    print()
    
    # Test Case 3: Insert at end
    print("Test Case 3: Insert 6 in [1, 3, 5]")
    head3 = solution.createList([1, 3, 5])
    print("Before insertion:")
    solution.printList(head3)
    head3 = solution.sortedInsert(head3, 6)
    print("After insertion:")
    solution.printList(head3)

if __name__ == "__main__":
    main()