**Extract Digits Present in the Given Number**

```python
n = int(input("Enter any number: "))
while n != 0:
    d = n % 10
    print(d)
    n = n // 10
```

**Sum of Digits Present in the Given Number**

```python
sum = 0
while n != 0:
    d = n % 10
    sum = sum + d
    n = n // 10
print(sum)

#Using List Comprehension for Sum of Digits
print(sum([int(i) for i in str(n)]))

# approach 3
def sumofdigits_v1(n):
    s = 0
    while n != 0:
        d = n % 10
        s = s + d
        n = n // 10
    return s

def sumofdigits_v2(n):
    return sum([int(i) for i in str(n)])
```

### **Example Usage**

```python
n = int(input("Enter any number: "))
print(f'Sum of digits present in {n} is {sumofdigits_v1(n)}')
print(f'Sum of digits present in {n} is {sumofdigits_v2(n)}')
```
