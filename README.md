# Modern_AI_Python
Python powers AI innovation in machine learning, deep learning, natural language processing, computer vision, and robotics. With TensorFlow, PyTorch, and scikit-learn, it enables automation, predictive analytics, and speech recognition. Its efficiency, flexibility, and community support drive AI advancements across industries.

[Modern AI Python - Github](https://github.com/panaversity/learn-modern-ai-python/tree/main/00_python_colab)

---
&nbsp;

### Key Differences Between Mutable and Immutable Types

**Mutable Data Types (Can Be Changed After Creation)**  `list`, `dict`, `set`, `bytearray`

**Immutable Data Types (Cannot Be Changed After Creation)** `int`, `float`, `str`, `tuple`, `frozenset`, `bytes`

| Feature               | Mutable (changeable)                | Immutable ()                                           |
| --------------------- | ----------------------------------- | ---------------------------------------------------- |
| **Can be changed?**   | ✅ Yes                               | ❌ No                                                 |
| **Memory efficient?** | 🚀 Can modify in place              | 📌 Creates new objects                               |
| **Hashable?**         | ❌ No *(except `frozenset`)*        | ✅ Yes *(used as dictionary keys)*                   |
| **Examples**          | `list`, `dict`, `set`, `bytearray`  | `int`, `float`, `str`, `tuple`, `frozenset`, `bytes` |

---
&nbsp;

### Python Data Types 

| Data Type                   | Ordered? | Changeable? | Allows Duplicates? | Category | Used to Store |
|-----------------------------|---------|-------------|-------------------|----------|---------------|
| **Set (`set {}`)**         | ❌ No  | ✅ Yes (Mutable) | ❌ No | Set | Unique items (any data type) |
| **Dictionary (`dict {}`)** | ✅ Yes (Python 3.7+) | ✅ Yes (Mutable) | ❌ No (Keys must be unique) | Mapping | Key-value pairs |
| **List (`list []`)**       | ✅ Yes  | ✅ Yes (Mutable) | ✅ Yes  | Sequence | Multiple items (any data type) |
| **Tuple (`tuple ()`)**     | ✅ Yes  | ❌ No (Immutable) | ✅ Yes | Sequence | Multiple items (any data type) |
| **String (`str '' or ""`)**  | ✅ Yes  | ❌ No (Immutable) | ✅ Yes | Sequence | Text data |

**Number Types:**  **`int`** - Integer (whole number), **`float`** - Floating-point number (decimal), **`complex`** - Complex number (e.g., `3 + 4j`)  

**Sequence Types:**  **`list`** - Ordered, mutable collection of items, **`tuple`** - Ordered, immutable collection of items, **`str`** - String (sequence of characters)  

**Mapping Type:**  **`dict`** - Dictionary (key-value pairs)  

**Set Types:**  **`set`** - Unordered collection of unique items, **`frozenset`** - Immutable set  

**Boolean Type:**  **`bool`** - Represents `True` or `False`  

**Special Types:**  **`NoneType`** - Represents no value (`None`), **`bytes`** - Immutable sequence of bytes, **`bytearray`** - Mutable sequence of bytes  

  
---
&nbsp;

## Python Operators  

### 1. Arithmetic Operators  
Perform mathematical calculations:  
- `+` (Addition): `5 + 3 = 8`  
- `-` (Subtraction): `5 - 3 = 2`  
- `*` (Multiplication): `5 * 3 = 15`  
- `/` (Division): `5 / 2 = 2.5`  
- `//` (Floor Division): `5 // 2 = 2`  (removes decimal part) 
- `%` (Modulus): `5 % 2 = 1` (returns remainder)  
- `**` (Exponentiation): `2 ** 3 = 8`

<br>

| Operator | Name                | Example                           |
|----------|---------------------|-----------------------------------|
| +        | Addition            | 5 + 2 = 7                         |
| -        | Subtraction         | 5 - 2 = 3                         |
| *        | Multiplication      | 5 * 2 = 10                        |
| /        | Division (float)    | 5 / 2 = 2.5                       |
| //       | Floor Division      | 5 // 2 = 2 (removes decimal part) |
| %        | Modulus (remainder) | 5 % 2 = 1                         |
| **       | Exponentiation      | 5 ** 2 = 25                       |
                               
<br>

### 2. Comparison (Relational) Operators  
Compare values and return `True` or `False`:  
- `==` (Equal to): `5 == 3` → `False`  
- `!=` (Not equal to): `5 != 3` → `True`  
- `>` (Greater than): `5 > 3` → `True`  
- `<` (Less than): `5 < 3` → `False`  
- `>=` (Greater than or equal to): `5 >= 3` → `True`  
- `<=` (Less than or equal to): `5 <= 3` → `False`  

### 3. Logical Operators  
Used to combine conditional statements:  
- `and`: Returns `True` if both conditions are `True` → `True and False` → `False`  
- `or`: Returns `True` if at least one condition is `True` → `True or False` → `True`  
- `not`: Reverses the Boolean value → `not True` → `False`  

### 4. Bitwise Operators  
Operate at the binary level:  
- `&` (Bitwise AND): `5 & 3` → `1` (Binary: `101 & 011 = 001`)  
- `|` (Bitwise OR): `5 | 3` → `7` (Binary: `101 | 011 = 111`)  
- `^` (Bitwise XOR): `5 ^ 3` → `6` (Binary: `101 ^ 011 = 110`)  
- `~` (Bitwise NOT): `~5` → `-6` (Inverts all bits)  
- `<<` (Left Shift): `5 << 1` → `10` (Binary: `1010`)  
- `>>` (Right Shift): `5 >> 1` → `2` (Binary: `10`)

   **`~x (Bitwise NOT)` is equivalent to `-(x + 1)` :**  `~` (Bitwise NOT): ~5 → -6 (Inverts all bits)  5=−(5+1)=−6

### 5. Identity Operators  
Check if two variables reference the same object in memory:  
- `is`: Returns `True` if both variables refer to the same object → `a is b`  
- `is not`: Returns `True` if they do not refer to the same object → `a is not b`

### 6. Membership Operators
Check if a value exists in a sequence (list, tuple, string, etc.):

- `in`: Returns True if a value is found → 2 in [1, 2, 3] → True
- `not in`: Returns True if a value is not found → 4 not in [1, 2, 3] → True
 
Example: Identity Operators  
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True (same memory reference)
print(a is c)  # False (different objects)
```
Example: Membership Operators 
```python
text = "Hello, Python!"
print("Python" in text)  # True
print("Java" not in text)  # True
```

### Explanation

### Logical Operators in Python (`and`, `or`, `not`)

Logical operators in Python are used to combine conditional statements and return Boolean values (`True` or `False`).

| Operator | Description | Example | Output |
|----------|------------|---------|--------|
| `and`   | Returns `True` if both conditions are `True` | `True and False` | `False` |
| `or`    | Returns `True` if at least one condition is `True` | `True or False` | `True` |
| `not`   | Reverses the Boolean value | `not True` | `False` |


### Identity Operators in Python (`is`, `is not`)

Identity operators in Python are used to compare the memory location of two objects.

| Operator | Description | Example | Output |
|----------|------------|---------|--------|
| `is`    | Returns `True` if both variables refer to the same object in memory | `a is b` | `True` |
| `is not` | Returns `True` if both variables refer to different objects in memory | `a is not b` | `True` |


### Membership Operators in Python

Membership operators in Python are used to check if a value exists in a sequence (such as a list, tuple, string, or dictionary).

- `in` checks if a value exists in a sequence.  
- `not in` checks if a value does **not** exist in a sequence.  

| Operator  | Description | Example | Output |
|-----------|------------|---------|--------|
| `in`      | Returns `True` if the value exists in the sequence | `"a" in "apple"` | `True` |
| `not in`  | Returns `True` if the value does not exist in the sequence | `"z" not in "apple"` | `True` |


## Difference Between `==` and `is` in Python  

- `==` **compares values** (checks if two objects have the same content).  
- `is` **compares identity** (checks if two variables point to the same memory location).  

### Comparison Table  

| Operator | Purpose | Example | Output |
|----------|---------|---------|--------|
| `==`    | Checks if values are equal | `[1, 2, 3] == [1, 2, 3]` | `True` |
| `is`    | Checks if two variables refer to the same object | `[1, 2, 3] is [1, 2, 3]` | `False` |

---
&nbsp;


