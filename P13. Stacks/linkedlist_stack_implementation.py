class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return -1
        top = self.head.data
        self.head = self.head.next
        return top

    def peek(self):
        if self.is_empty():
            return -1
        return self.head.data


# Main function to test the Stack
if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    while not s.is_empty():
        print(s.peek())
        s.pop()

# Dry Run:
# Initial Stack: []
# After s.push(1): [1]
# After s.push(2): [2, 1]
# After s.push(3): [3, 2, 1]
# After s.push(4): [4, 3, 2, 1]
# Peek and Pop sequence:
# Peek: 4, Pop: [3, 2, 1]
# Peek: 3, Pop: [2, 1]
# Peek: 2, Pop: [1]
# Peek: 1, Pop: []
# Stack is now empty.
