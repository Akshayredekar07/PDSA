class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return len(self.list) == 0

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.is_empty():
            return -1
        return self.list.pop()

    def peek(self):
        if self.is_empty():
            return -1
        return self.list[-1]


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
