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


if __name__ == "__main__":
    s = Stack()
    s.push(1)  # Stack: [1]
    s.push(2)  # Stack: [1, 2]
    s.push(3)  # Stack: [1, 2, 3]
    s.push(4)  # Stack: [1, 2, 3, 4]

    while not s.is_empty():
        print(s.peek())  # Outputs: 4, then 3, then 2, then 1
        s.pop()          # Stack after each pop: [1, 2, 3], [1, 2], [1], []

# Dry Run Results:
# 1. After pushing 1, 2, 3, 4, the stack is [1, 2, 3, 4].
# 2. The first print outputs 4, then pops it, stack becomes [1, 2, 3].
# 3. The second print outputs 3, then pops it, stack becomes [1, 2].
# 4. The third print outputs 2, then pops it, stack becomes [1].
# 5. The fourth print outputs 1, then pops it, stack becomes [].
# 6. The loop ends as the stack is now empty.
