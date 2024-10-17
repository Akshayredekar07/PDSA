## Algorithm

**Definition:**
A step-by-step process for solving any problem is called an algorithm.

### Example: Addition of Three Numbers

**Algorithm:**
1. Read 'a' value from the user.
2. Read 'b' value from the user.
3. Read 'c' value from the user.
4. Calculate `sum = a + b + c`.
5. Print or return the result `sum`.

---

### Flowchart

A diagrammatic or pictorial representation of an algorithm is called a flowchart.

---

### Implementation

```python
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
sum = a + b + c
print(f"sum = {sum}")
```

### Sample Output:

```bash
C:\8pm>py test.py
Enter a value: 10
Enter b value: 20
Enter c value: 30
sum = 60
```

---

### Advantages of Algorithm/Flowchart

1. The problem will be simplified.
2. Easy to understand the problem statement.
3. Easy to implement.
4. Provides a format/template/pattern to solve the problem.

---

### Properties of an Algorithm

1. Zero or more inputs.
2. One or more outputs (at least one output should be present).
3. Deterministic (same output for the same input repeatedly).
4. Correct.
5. Terminates after finite steps (has a base condition).
6. Efficient (the logic should be clear).


### Complexity

**Definition:**
The complexity of an algorithm is the amount of time or space required by the algorithm or program to process the inputs and produce the output.

### Types of Complexity:

1. **Time Complexity**
2. **Space Complexity**

---

### Time Complexity

The amount of time taken by the algorithm to process the inputs is called time complexity, which is measured using `T(n)`.

---

### Space Complexity

The amount of space taken by the algorithm to process the inputs is called space complexity, which is measured using `S(n)`.

---

## Asymptotic Notations

- **Big-Oh notation:** O(n)
- **Omega notation:** Ω(n)
- **Theta notation:** Θ(n)

---

### Algorithm Classifications by Complexity:

1. **Worst Case Complexity**
2. **Average Case Complexity**
3. **Best Case Complexity**

### Common Time Complexities:

- O(1) - Constant time
- O(n) - Linear time
- O(log n) - Logarithmic time
- O(n log n) - Log-linear time
- O(n²) - Quadratic time
- O(2ⁿ) - Exponential time
- O(n!) - Factorial time

---

### Example 1:

```python
def fun(n):
    c = 0
    i = 0
    while i < n:
        c = c + 1
        i = i + 1
    return c

print("N=100, number of instructions in O(n): ", fun(100))
```

**Output:**

```bash
C:\8pm>py test.py
N=100, number of instructions in O(n):  100
```

**Complexity:** O(n)

---

### Example 2:

```python
def fun(n):
    c = 0
    i = 0
    while i < n:
        j = 0
        while j < n:
            c = c + 1
            j = j + 1
        i = i + 1
    return c

print("N=100, number of instructions in O(n²): ", fun(100))
```

**Complexity:** O(n²)

---

### Example 3:

```python
# Half iterations
def fun(n):
    c = 0
    i = n
    while i > 0:
        c = c + 1
        i = i // 2
    return c

print("N=100, number of instructions in O(log n): ", fun(100))  # 7
```

**Complexity:** O(log n)

---

### Example 1: Convert Even Indexed Characters to Upper Case

**Input:** `abc` → **Output:** `AbC`  
**Input:** `abcd` → **Output:** `AbCd`  
**Input:** `abcde` → **Output:** `AbCdE`

```python
def myfun(s):
    l = list(s.lower())
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l[i].upper()
    return ''.join(l)

s = "prakash BaBu"
print(s)          # prakash BaBu
print(myfun(s))   # PrAkAsH BaBu
```

---

### Example 2: Convert Odd Indexed Characters to Upper Case

**Input:** `abc` → **Output:** `aBc`  
**Input:** `abcd` → **Output:** `aBcD`  
**Input:** `abcde` → **Output:** `aBcDe`

```python
def myfun(s):
    l = list(s.lower())
    for i in range(len(l)):
        if i % 2 != 0:
            l[i] = l[i].upper()
    return ''.join(l)

s = "prakash BaBu"
print(s)          # prakash BaBu
print(myfun(s))   # pRaKaSh bAbU
```
