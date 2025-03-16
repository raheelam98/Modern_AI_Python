# Modern_AI_Python
Python powers AI innovation in machine learning, deep learning, natural language processing, computer vision, and robotics. With TensorFlow, PyTorch, and scikit-learn, it enables automation, predictive analytics, and speech recognition. Its efficiency, flexibility, and community support drive AI advancements across industries.

[Modern AI Python - Github](https://github.com/panaversity/learn-modern-ai-python/tree/main/00_python_colab)

---

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

### Python Data Types Table

| Data Type                   | Ordered? | Changeable? | Allows Duplicates? | Category | Used to Store |
|-----------------------------|---------|-------------|-------------------|----------|---------------|
| **Set (`set {}`)**         | ❌ No  | ✅ Yes (Mutable) | ❌ No | Set | Unique items (any data type) |
| **Dictionary (`dict {}`)** | ✅ Yes (Python 3.7+) | ✅ Yes (Mutable) | ❌ No (Keys must be unique) | Mapping | Key-value pairs |
| **List (`list []`)**       | ✅ Yes  | ✅ Yes (Mutable) | ✅ Yes  | Sequence | Multiple items (any data type) |
| **Tuple (`tuple ()`)**     | ✅ Yes  | ❌ No (Immutable) | ✅ Yes | Sequence | Multiple items (any data type) |
| **String (`str '' or ""`)**  | ✅ Yes  | ❌ No (Immutable) | ✅ Yes | Sequence | Text data |

---

## Python Operators  

## 1. Arithmetic Operators  
Perform mathematical calculations:  
- `+` (Addition): `5 + 3 = 8`  
- `-` (Subtraction): `5 - 3 = 2`  
- `*` (Multiplication): `5 * 3 = 15`  
- `/` (Division): `5 / 2 = 2.5`  
- `//` (Floor Division): `5 // 2 = 2`  
- `%` (Modulus): `5 % 2 = 1` (returns remainder)  
- `**` (Exponentiation): `2 ** 3 = 8`  

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

