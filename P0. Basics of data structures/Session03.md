## Example 3: Find Sum of All Elements Present in a List

```python
import functools

def fun_version1(L):
    s = 0
    for i in L:
        s = s + i
    return s

def fun_version2(L):
    return sum(L)

def fun_version3(L):
    return functools.reduce(lambda i, j: i + j, L)

L = [11, 22, 33, 44, 55]
print(fun_version1(L))  # 11 + 22 + 33 + 44 + 55 = 165
print(fun_version2(L))  # 11 + 22 + 33 + 44 + 55 = 165
print(fun_version3(L))  # 11 + 22 + 33 + 44 + 55 = 165
```

---

## Example 4: Find Max of Two Numbers

```python
def maxfun_version1(a, b):
    return max(a, b)

def maxfun_version2(a, b):
    return a if a > b else b

def maxfun_version3(a, b):
    if a > b:
        return a
    else:
        return b

def maxfun_version4(a, b):
    call = lambda a, b: a if a > b else b
    return call(a, b)

def maxfun_version5(a, b):
    L = []
    L.append(a)
    L.append(b)
    return max(L)

a = int(input())
b = int(input())
print("Max value by using version1:", maxfun_version1(a, b)) 
print("Max value by using version2:", maxfun_version2(a, b)) 
print("Max value by using version3:", maxfun_version3(a, b)) 
print("Max value by using version4:", maxfun_version4(a, b)) 
print("Max value by using version5:", maxfun_version5(a, b)) 
```

### Sample Output:

```bash
C:\dsapb>py test.py
1
2
Max value by using version1: 2
Max value by using version2: 2
Max value by using version3: 2
Max value by using version4: 2
Max value by using version5: 2

C:\dsapb>py test.py
1
-2
Max value by using version1: 1
Max value by using version2: 1
Max value by using version3: 1
Max value by using version4: 1
Max value by using version5: 1
```

## Case 1: Insert a New Node at the Beginning of a Singly Linked List

```python
def add_first(self, value):
    newnode = self.node(value, None)
    if self.head == None:
        self.head = newnode
        return
    newnode.next = self.head
    self.head = newnode
```

---

## Case 2: Insert a New Node at the End of a Singly Linked List

```python
def add_last(self, value):
    newnode = self.node(value, None)
    if self.head == None:
        self.head = newnode
        return
    temp = self.head
    while temp.next != None:
        temp = temp.next
    temp.next = newnode
```

---

## Case 3: Traverse or Display a Singly Linked List

```python
def display(self):
    temp = self.head
    if temp == None:
        print("SLL is empty")
        return
    while temp != None:
        print(temp.data)
        temp = temp.next
```

---

## Example 5: Find Min of Two Numbers

```python
def minfun_version1(a, b):
    return min(a, b)

def minfun_version2(a, b):
    return a if a < b else b

def minfun_version3(a, b):
    if a < b:
        return a
    else:
        return b

def minfun_version4(a, b):
    call = lambda a, b: a if a < b else b
    return call(a, b)

def minfun_version5(a, b):
    L = []
    L.append(a)
    L.append(b)
    return min(L)

a = int(input())
b = int(input())
print("Min value by using version1:", minfun_version1(a, b)) 
print("Min value by using version2:", minfun_version2(a, b)) 
print("Min value by using version3:", minfun_version3(a, b)) 
print("Min value by using version4:", minfun_version4(a, b)) 
print("Min value by using version5:", minfun_version5(a, b)) 
```

### Sample Output:

```bash
C:\dsapb>py test.py
10
20
Min value by using version1: 10
Min value by using version2: 10
Min value by using version3: 10
Min value by using version4: 10
Min value by using version5: 10
```

## Example 6: Find Max of Three Numbers

```python
def maxfun_version1(a, b, c):
    return max(a, b, c)

def maxfun_version2(a, b, c):
    return a if a > b and a > c else b if b > c else c

def maxfun_version3(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

def maxfun_version4(a, b, c):
    call = lambda a, b, c: a if a > b and a > c else b if b > c else c
    return call(a, b, c)

def maxfun_version5(a, b, c):
    L = [a, b, c]
    return max(L)

a = int(input())
b = int(input())
c = int(input())
print("Max value by using version1:", maxfun_version1(a, b, c)) 
print("Max value by using version2:", maxfun_version2(a, b, c)) 
print("Max value by using version3:", maxfun_version3(a, b, c)) 
print("Max value by using version4:", maxfun_version4(a, b, c)) 
print("Max value by using version5:", maxfun_version5(a, b, c))
```

---

## Example 7: WPP to Find Min of Three Numbers

```python
def minfun_version1(a, b, c):
    return min(a, b, c)

def minfun_version2(a, b, c):
    return a if a < b and a < c else b if b < c else c

def minfun_version3(a, b, c):
    if a < b and a < c:
        return a
    elif b < c:
        return b
    else:
        return c

def minfun_version4(a, b, c):
    call = lambda a, b, c: a if a < b and a < c else b if b < c else c
    return call(a, b, c)

def minfun_version5(a, b, c):
    L = [a, b, c]
    return min(L)
```

---

## Example 8: WPP to Find Max of Four Numbers

```python
def maxfun_version1(a, b, c, d):
    return max(a, b, c, d)

def maxfun_version2(a, b, c, d):
    return a if a > b and a > c and a > d else b if b > c and b > d else c if c > d else d

def maxfun_version3(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > c and b > d:
        return b
    elif c > d:
        return c
    else:
        return d

def maxfun_version4(a, b, c, d):
    call = lambda a, b, c, d: a if a > b and a > c and a > d else b if b > c and b > d else c if c > d else d
    return call(a, b, c, d)

def maxfun_version5(a, b, c, d):
    L = [a, b, c, d]
    return max(L)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("Max value by using version1:", maxfun_version1(a, b, c, d)) 
print("Max value by using version2:", maxfun_version2(a, b, c, d)) 
print("Max value by using version3:", maxfun_version3(a, b, c, d)) 
print("Max value by using version4:", maxfun_version4(a, b, c, d)) 
print("Max value by using version5:", maxfun_version5(a, b, c, d))
```

---

## Example 9: WPP to Find Min of Four Numbers

```python
def minfun_version1(a, b, c, d):
    return min(a, b, c, d)

def minfun_version2(a, b, c, d):
    return a if a < b and a < c and a < d else b if b < c and b < d else c if c < d else d

def minfun_version3(a, b, c, d):
    if a < b and a < c and a < d:
        return a
    elif b < c and b < d:
        return b
    elif c < d:
        return c
    else:
        return d

def minfun_version4(a, b, c, d):
    call = lambda a, b, c, d: a if a < b and a < c and a < d else b if b < c and b < d else c if c < d else d
    return call(a, b, c, d)

def minfun_version5(a, b, c, d):
    L = [a, b, c, d]
    return min(L)
```

---

## Example 10: WPP to Find Max of Five Numbers
## Example 11: WPP to Find Min of Five Numbers
## Example 12: WPP to Find the Difference Between Max and Min of Five Numbers

```python
def diff_max_min(L):
    return max(L) - min(L)
```

---

## Example 13: WPP to Find the Factorial of a Given Number

```python
# Ex13: WPP to find factorial of the given number

# Logic 1: Using While Loop
def factorial_logic1(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i = i + 1
    return f

# Logic 2: Using Recursion
def factorial_logic2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_logic2(n - 1)

# Logic 3: Using Predefined Functions
import math
def factorial_logic3(n):
    return math.factorial(n)

# Main Code
for i in range(10 + 1):
    print(i, factorial_logic1(i), factorial_logic2(i), factorial_logic3(i), sep='\t\t')
```


### Ex14: WPP to check whether the given number is prime or not
```py

# Optimized Logic 1: By Using Loops
def isprime1(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check up to the square root of n
        if n % i == 0:
            return False
    return True

# Dry Run for isprime1
# Example: n = 7
# 1. Check if 7 <= 1: False
# 2. Loop i from 2 to 2 (int(7**0.5) + 1)
#    - i = 2: 7 % 2 != 0 (continue)
# 3. Loop ends, return True (7 is prime)

# Optimized Logic 2: By Using Recursion
def isprime2(n, i=None):
    if n <= 1:
        return False
    if i is None:
        i = int(n**0.5)  # Start checking from the square root of n
    if i < 2:
        return True
    if n % i == 0:
        return False
    return isprime2(n, i - 1)

# Dry Run for isprime2
# Example: n = 7
# 1. Check if 7 <= 1: False
# 2. i is None, set i = 2 (int(7**0.5))
# 3. Check if i < 2: False
# 4. Check if 7 % 2 != 0: True, call isprime2(7, 1)
# 5. Check if 7 <= 1: False
# 6. Check if i < 2: True, return True (7 is prime)

# Main Code
for i in range(2, 11):
    print(f"i={i}\t{isprime1(i)}\t{isprime2(i)}")
``