def push_at_bottom(stack, data):
    if not stack:
        stack.append(data)
        return
    top = stack.pop()
    push_at_bottom(stack, data)
    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    push_at_bottom(stack, top)


def print_stack(stack):
    while stack:
        print(stack.pop())


# Main function to test the stack reversal
if __name__ == "__main__":
    stack = []
    stack.append(1)
    stack.append(2)
    stack.append(3)

    reverse_stack(stack)
    print_stack(stack)
