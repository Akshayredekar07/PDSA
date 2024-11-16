def reverse_string(s):
    stack = []
    
    # Push all characters of the string onto the stack
    for char in s:
        stack.append(char)
    
    # Pop characters from the stack and build the reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str


# Main function to test the reverse_string function
if __name__ == "__main__":
    string = "abc"
    result = reverse_string(string)
    print(result)
