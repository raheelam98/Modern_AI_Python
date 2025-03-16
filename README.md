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

