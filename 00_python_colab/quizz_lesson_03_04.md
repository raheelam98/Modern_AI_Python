### Lesson_03_04

## Python Quiz Questions

#### **What will be the output of `~5` in Python?**
Select one answer A) 4 B) -6 C) 5 D) -5

#### **Which of the following is a binary operator?**
Select one answer A) `+` B) `-` C) `*` D) All of the above

#### **What does the `//` operator do in Python?**
Select one answer A) Exponentiation B) Floor division C) Modulus D) Division

#### **What is the output of `8 % 3`?**
Select one answer A) 2 B) 5 C) 3 D) 8

#### **What will `5 == 5.0` return in Python?**
Select one answer A) True B) False C) Error D) None

#### **What is the result of `8 <= 8`?**
Select one answer A) True B) False C) None D) Error

#### **What is the output of `not (True or False)`?**
Select one answer A) True B) False C) None D) Error

#### **What is the meaning of `x //= 3`?**
Select one answer A) `x = x / 3` B) `x = x * 3` C) `x = x // 3` D) `x = x % 3`

#### **What is the result of `x *= 2` when `x = 4`?**
Select one answer A) 6 B) 8 C) 4 D) 2

#### **Which of the following is an identity operator?**
Select one answer A) `==` B) `is` C) `!=` D) `>=`

#### **What is the difference between `==` and `is`?**
Select one answer A) `==` checks value equality, `is` checks reference B) `is` checks value equality, `==` checks reference C) They are the same D) `is` is used only for numbers

#### **Which of the following is a membership operator?**
Select one answer A) `in` B) `not in` C) Both A and B D) None of the above

#### **What is the result of `'a' in 'apple'`?**
Select one answer A) True B) False C) None D) Error

#### **What will `'z' not in 'pizza'` return?**
Select one answer A) True B) False C) None D) Error

###### **Which membership operator checks if an element exists in a sequence?**
Select one answer A) `in` B) `not in` C) `is` D) `==`

# Explanation

**The ~ (bitwise NOT) operator in Python inverts all bits of a number and is equivalent to -(n+1).**

### Binary Operators in Python  

A **binary operator** is an operator that operates on **two operands**.  

## Examples of Binary Operators in Python  

### 1. Arithmetic Operators  
- `+` (Addition): `5 + 3 = 8`  
- `-` (Subtraction): `5 - 3 = 2`  
- `*` (Multiplication): `5 * 3 = 15`  
- `/` (Division): `5 / 2 = 2.5`  
- `//` (Floor Division): `5 // 2 = 2`  
- `%` (Modulus): `5 % 2 = 1`  
- `**` (Exponentiation): `2 ** 3 = 8`

### 2. Comparison (Relational) Operators  
- `==` (Equal to): `5 == 3 → False`  
- `!=` (Not equal to): `5 != 3 → True`  
- `>` (Greater than): `5 > 3 → True`  
- `<` (Less than): `5 < 3 → False`  
- `>=` (Greater than or equal to): `5 >= 3 → True`  
- `<=` (Less than or equal to): `5 <= 3 → False`  

### 3. Logical Operators  
- `and`: `True and False → False`  
- `or`: `True or False → True` 

### 4. Bitwise Operators  
- `&` (Bitwise AND): `5 & 3 → 1`  
- `|` (Bitwise OR): `5 | 3 → 7`  
- `^` (Bitwise XOR): `5 ^ 3 → 6`  
- `<<` (Left Shift): `5 << 1 → 10`  
- `>>` (Right Shift): `5 >> 1 → 2`

### Key Point  
A **binary operator** always requires **two operands** (e.g., `a + b`), whereas a **unary operator** (like `not`, `+x`, `-x`, `~x`) operates on **only one operand**.  

#### **modulus (%) operator in Python returns the remainder of a division.**

What is the output of 8 % 3? 8÷3=2 (quotient), remainder 2  

#### `//=` Operator in Python (floor division) 
**// (floor division) operator in Python performs division but rounds down to the nearest whole number (integer).**

What is the result of 15 // 4?   15÷4=3.75  
Since floor division rounds down to the nearest integer, the result is 3.

The `//=` operator is a **floor division assignment operator** in Python. It performs **floor division** and then assigns the result back to `x`.  

#### Syntax  
```python
x //= 3  # This is the same as: x = x // 3
```

## Logical Operators in Python  (and, or , not)

Logical operators in Python are used to combine conditional statements and return Boolean values (`True` or `False`).  

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `and` | Returns `True` if **both** conditions are `True` | `True and False` | `False` |
| `or` | Returns `True` if **at least one** condition is `True` | `True or False` | `True` |
| `not` | Reverses the Boolean value | `not True` | `False` |

### `and` Operator  
```python
print(True and False)  # Output: False
print(True and True)   # Output: True
```

## Identity Operators in Python  (is, is not)

Identity operators in Python are used to **compare the memory location** of two objects.  

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `is` | Returns `True` if both variables refer to the **same object** in memory | `a is b` | `True` |
| `is not` | Returns `True` if both variables refer to **different objects** in memory | `a is not b` | `True` |

### `is` Operator  
```python
a = [1, 2, 3]
b = a  # Both 'a' and 'b' point to the same object in memory
print(a is b)  # Output: True
```

### `is not` Operator
```python
x = [1, 2, 3]
y = [1, 2, 3]  # Different objects with the same values
print(x is not y)  # Output: True
```

## Difference Between `==` and `is` in Python  

In Python, `==` and `is` are used for different purposes:  

- `==` **compares values**
   checks if **values are the same**, even if the objects are different.
   `==` when you want to **compare values**.
  
- `is` **compares object identity (memory location)**
   checks if **both variables refer to the exact same object in memory**.
   `is` when you want to check if two variables refer to the **same object in memory**.

  ### Key Differences: is vs ==
* Use **`is`** when checking object identity (same memory location).
* Use **`==`** when checking if values are the same.

## Comparison Table  

| Operator | Purpose | Example | Output |
|----------|---------|---------|--------|
| `==` | Checks if values are equal | `[1, 2, 3] == [1, 2, 3]` | `True` |
| `is` | Checks if two variables refer to the same object in memory | `[1, 2, 3] is [1, 2, 3]` | `False` |

#### Example Code  
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a  # c points to the same object as a

print(a == b)  # Output: True (Values are the same)
print(a is b)  # Output: False (Different memory locations)

print(a is c)  # Output: True (Same memory location)
```

## Membership Operators in Python  

Membership operators in Python are used to check if a value exists in a **sequence** (such as a list, tuple, string, or dictionary).  

- **in** checks if a **value exists in a sequence**.
- **not in** checks if a **value does NOT exist in a sequence**.

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `in` | Returns `True` if the value exists in the sequence | `"a" in "apple"` | `True` |
| `not in` | Returns `True` if the value does not exist in the sequence | `"z" not in "apple"` | `True` |

#### Example Code  

```python
# Using 'in'
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)  # Output: True

# Using 'not in'
print("grape" not in fruits)  # Output: True
```


