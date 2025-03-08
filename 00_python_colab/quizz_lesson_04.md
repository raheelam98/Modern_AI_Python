

### Lesson_04

What will be the output of ~5 in Python?
Select one answer
A) 4
B) -6
C) 5
D) -5

Which of the following is a binary operator?
Select one answer
A) +
B) -
C) *
D) All of the above

What does the // operator do in Python?
Select one answer
A) Exponentiation
B) Floor division
C) Modulus
D) Division

What is the output of 8 % 3?
Select one answer
A) 2
B) 5
C) 3
D) 8

What will 5 == 5.0 return in Python?
Select one answer
A) True
B) False
C) Error
D) None

What is the result of 8 <= 8?
Select one answer
A) True
B) False
C) None
D) Error

What is the output of not (True or False)?
Select one answer
A) True
B) False
C) None
D) Error

What is the meaning of x //= 3?
Select one answer
A) x = x / 3
B) x = x * 3
C) x = x // 3
D) x = x % 3

What is the result of x *= 2 when x = 4?
Select one answer
A) 6
B) 8
C) 4
D) 2

Which of the following is an identity operator?
Select one answer
A) ==
B) is
C) !=
D) >=


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

modulus (%) operator in Python returns the remainder of a division.
What is the output of 8 % 3? 8÷3=2 (quotient), remainder 2   

// (floor division) operator in Python performs division but rounds down to the nearest whole number (integer).
What is the result of 15 // 4?   15÷4=3.75  
Since floor division rounds down to the nearest integer, the result is 3.


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

## Key Point  
A **binary operator** always requires **two operands** (e.g., `a + b`), whereas a **unary operator** (like `not`, `+x`, `-x`, `~x`) operates on **only one operand**.  


### Logical Operators in Python  

Logical operators in Python are used to combine conditional statements and return Boolean values (`True` or `False`).  

## Logical Operators  

| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `and` | Returns `True` if **both** conditions are `True` | `True and False` | `False` |
| `or` | Returns `True` if **at least one** condition is `True` | `True or False` | `True` |
| `not` | Reverses the Boolean value | `not True` | `False` |

## Examples  

### `and` Operator  
```python
print(True and False)  # Output: False
print(True and True)   # Output: True
```

### `//=` Operator in Python  

The `//=` operator is a **floor division assignment operator** in Python. It performs **floor division** and then assigns the result back to `x`.  

#### Syntax  
```python
x //= 3  # This is the same as: x = x // 3
```

## Identity Operators in Python  

Identity operators in Python are used to **compare the memory location** of two objects.  

## Identity Operators  
| Operator | Description | Example | Output |
|----------|-------------|---------|--------|
| `is` | Returns `True` if both variables refer to the **same object** in memory | `a is b` | `True` |
| `is not` | Returns `True` if both variables refer to **different objects** in memory | `a is not b` | `True` |

## Example Usage  

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


