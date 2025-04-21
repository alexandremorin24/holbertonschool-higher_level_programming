# 🧠 Understanding Python Objects: Identity, Mutability, and Function Behavior

![Python Objects](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)

## 🔍 Introduction

If you've ever wondered how Python treats variables behind the scenes, this project on "everything is object" is a deep dive into that world. It covers how variables relate to objects, how Python handles mutable and immutable types, and what really happens when values are passed into functions. Understanding these foundational concepts is crucial for writing bug-free, efficient Python code—especially when working with complex data structures.

---

## 🪪 `id` and `type`: How Python Identifies Objects

In Python, **everything is an object**, and two fundamental built-in functions help you explore them:

```python
type(obj)  # tells you the type
id(obj)    # returns the identity (memory address)
```

Example:

```python
a = 42
print(type(a))  # <class 'int'>
print(id(a))    # (some memory address)
```

Small integers and some strings are interned:

```python
a = 100
b = 100
print(id(a) == id(b))  # True
```

---

## 🔄 Mutable Objects

Mutable objects can be changed in place. Lists are a perfect example:

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4]
```

Both `l1` and `l2` point to the **same object**.

```python
print(l1 is l2)  # True
```

---

## 🔒 Immutable Objects

Immutable objects (like `int`, `str`, `tuple`) cannot be changed after creation:

```python
a = 89
b = a
a += 1
print(a)  # 90
print(b)  # 89
print(a is b)  # False
```

Strings are also immutable:

```python
s1 = "Hello"
s2 = s1
s1 += " World"
print(s2)  # Hello
```

---

## 🤔 Why It Matters: Mutability vs Immutability

Python handles mutable and immutable objects differently in memory:

```python
a = [1, 2, 3]
print(id(a))       # e.g., 139...
a = a + [4]
print(id(a))       # New object
```

With `+=`, the object is modified in place:

```python
a = [1, 2, 3]
print(id(a))
a += [4]
print(id(a))       # Same object
```

This is essential to understand when passing arguments into functions.

---

## 🧩 Function Arguments: Mutable vs Immutable

Python passes everything **by assignment**. That’s why this doesn’t change the original:

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)  # 1
```

But this does:

```python
def add_item(lst):
    lst.append(4)

nums = [1, 2, 3]
add_item(nums)
print(nums)  # [1, 2, 3, 4]
```

However, reassignment inside a function won’t affect the outside:

```python
def assign_new(lst):
    lst = [4, 5, 6]

my_list = [1, 2, 3]
assign_new(my_list)
print(my_list)  # [1, 2, 3]
```

---

## 🚀 Bonus: Copying and Tuples

To copy a list:

```python
def copy_list(a_list):
    return a_list[:]
```

For tuples:

```python
a = (1)
print(type(a))  # <class 'int'>

a = (1,)
print(type(a))  # <class 'tuple'>
```

A single-element tuple needs a comma.

---

## 🧠 Conclusion

This project helped me deeply understand Python's object model. I now see the differences between identity and equality, between mutable and immutable objects, and how Python's internal mechanisms impact how we write and debug code.
