
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next

if __name__ == "__main__":
    head = None
    head = insert_at_begin(head, 30)
    head = insert_at_begin(head, 20)
    head = insert_at_begin(head, 10)

    x = 5
    head = insert_at_begin(head, x)

    print_list(head)