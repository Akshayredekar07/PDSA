# # Function to reverse a number using digit extraction
# def reverse_v1(n):
#     r = 0
#     while n != 0:
#         d = n % 10  # Extract the last digit
#         r = r * 10 + d  # Append the digit to the reversed number
#         n = n // 10  # Remove the last digit
#     return r

# # Function to reverse a number using string slicing
# def reverse_v2(n):
#     return int(str(n)[::-1])  # Convert the number to string, reverse it, then convert back to int

# # Main program
# n = int(input("Enter any number: "))
# print(f"Reverse of {n} using logic1 is {reverse_v1(n)}")
# print(f"Reverse of {n} using logic2 is {reverse_v2(n)}")




"""
# Function to check if a number is a palindrome using digit extraction
def ispali_v1(n):
    temp = n 
    r = 0
    while n != 0:
        d = n % 10  # Extract the last digit
        r = r * 10 + d  # Append the digit to the reversed number
        n = n // 10  # Remove the last digit
    return r == temp  # Compare the reversed number with the original


def ispali_v1(n):
    r, temp = 0, n  # Initialize reversed number and store original number
    while n:
        r = r * 10 + n % 10  # Extract and append digit
        n //= 10  # Remove last digit
    return r == temp  # Check if reversed number equals original


# Function to check if a number is a palindrome using string manipulation
def ispali_v2(n):
    s = str(n)  # Convert the number to a string
    return s == s[::-1]  # Check if the string is equal to its reverse

# Main program
n = int(input("Enter any number: "))
print(f"Is {n} a palindrome (logic1)? {ispali_v1(n)}")
print(f"Is {n} a palindrome (logic2)? {ispali_v2(n)}")

"""



# #Function to check digit presence using digit extraction
def fun1(n, key):
    flag = False
    while n != 0:
        d = n % 10
        if d == key:
            flag = True
            break
        n = n // 10
    return flag


def fun1(n, key):
    while n:
        if n % 10 == key:
            return True
        n //= 10
    return False


def fun2(n, key):
    return str(key) in str(n)

n = int(input("Enter any number: "))
key = int(input("Enter digit to check: "))
print(f"Is digit {key} in number {n} (logic1)? {fun1(n, key)}")
print(f"Is digit {key} in number {n} (logic2)? {fun2(n, key)}")


