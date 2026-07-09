# Java → Python Cheat Sheet (for Java devs)

## 1. Syntax Basics

| Java | Python |
|---|---|
| `{ }` blocks | Indentation (4 spaces) |
| `;` end of line | No semicolons |
| `// comment` | `# comment` |
| `String s = "hi";` | `s = "hi"` (no type declaration needed) |
| `final int X = 5;` | `X = 5` (convention: UPPER_CASE = constant, not enforced) |
| `System.out.println(x);` | `print(x)` |
| `null` | `None` |
| `true / false` | `True / False` |
| `&&  \|\| !` | `and  or  not` |
| `==` (value equality for primitives) | `==` (value equality for everything) |
| `.equals()` | `==` (Python's `==` calls `__eq__`, so no separate method needed) |
| `instanceof` | `isinstance(x, Type)` |

---

## 2. Variables & Types
Python is dynamically typed but you *can* add type hints (recommended, closest thing to Java's safety):

```python
def add(a: int, b: int) -> int:
    return a + b

name: str = "Alice"
```

No compiler enforcement — hints are for readability/tools (mypy) only.

---

## 3. Control Flow

```python
# if/elif/else
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# for loop (like enhanced for-each — there's no classic C-style for)
for item in my_list:
    print(item)

for i in range(10):      # like for(int i=0; i<10; i++)
    print(i)

# while
while x < 10:
    x += 1               # no x++ or ++x in Python!

# switch → match (Python 3.10+)
match day:
    case "MON" | "TUE":
        print("early week")
    case _:
        print("other")
```

---

## 4. Collections

| Java | Python |
|---|---|
| `ArrayList<Integer>` | `list` → `[1, 2, 3]` |
| `HashMap<K,V>` | `dict` → `{"a": 1}` |
| `HashSet<T>` | `set` → `{1, 2, 3}` |
| `int[] arr = new int[5];` | `arr = [0]*5` or `[0 for _ in range(5)]` |
| `list.add(x)` | `list.append(x)` |
| `list.get(i)` | `list[i]` |
| `map.get(key)` | `d[key]` or `d.get(key, default)` |
| `map.put(k, v)` | `d[k] = v` |
| `map.containsKey(k)` | `k in d` |
| Immutable list | `tuple` → `(1, 2, 3)` |

Python also has **list/dict comprehensions** (huge idiom — use these instead of manual loops):
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
squared_map = {x: x**2 for x in range(5)}
```

---

## 5. Functions

```python
def greet(name, greeting="Hello"):   # default args, no overloading needed
    return f"{greeting}, {name}!"

greet("Bob")                # "Hello, Bob!"
greet("Bob", greeting="Hi") # keyword args
```

- No method overloading — use default args or `*args`/`**kwargs`.
- `*args` = varargs (`String... args`), `**kwargs` = named/keyword args (no direct Java equivalent).

```python
def foo(*args, **kwargs):
    print(args)     # tuple
    print(kwargs)   # dict
```

---

## 6. Classes / OOP

```python
class Animal:
    def __init__(self, name):    # constructor
        self.name = name           # no need to declare fields beforehand

    def speak(self):              # 'self' = 'this', but explicit param
        raise NotImplementedError

class Dog(Animal):                 # inheritance
    def speak(self):
        return f"{self.name} says Woof"

d = Dog("Rex")
print(d.speak())
```

Key differences:
- No `public/private/protected` keywords. Convention: `_var` = "protected" (soft), `__var` = name-mangled (pseudo-private).
- No interfaces — use **Abstract Base Classes** (`abc` module) or just duck typing.
- `@staticmethod`, `@classmethod` decorators replace `static` methods.
- Everything is public by default.
- No method overloading; use default args or `@singledispatch`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

---

## 7. Exceptions

```java
try {
    risky();
} catch (IOException e) {
    handle(e);
} finally {
    cleanup();
}
```

```python
try:
    risky()
except IOError as e:
    handle(e)
finally:
    cleanup()
```

- No checked exceptions — you don't declare `throws`.
- `except Exception as e:` catches broadly (like `catch (Exception e)`).
- `raise ValueError("bad input")` instead of `throw new IllegalArgumentException(...)`.

---

## 8. Strings

```python
name = "World"
print(f"Hello, {name}!")        # f-strings — like String.format but cleaner
"  hi  ".strip()                 # .trim()
"a,b,c".split(",")               # ["a", "b", "c"]
",".join(["a", "b", "c"])        # "a,b,c" (no Java equivalent syntax, very common idiom)
str(123)                         # like String.valueOf / Integer.toString
```

---

## 9. Null Handling

- No `Optional<T>` ceremony (though `Optional`-like patterns exist) — just use `None` and check.
```python
x = maybe_get_value()
if x is not None:
    use(x)
```
- No `NullPointerException` — you get `AttributeError` if you call a method on `None`.

---

## 10. Imports / Packages

| Java | Python |
|---|---|
| `import java.util.List;` | `import module` or `from module import name` |
| `package com.example;` | Folder structure + `__init__.py` (or just modules in a package dir) |
| Maven/Gradle | `pip` + `requirements.txt` / `pyproject.toml` |

```python
import math
from collections import defaultdict, Counter
from typing import List, Dict, Optional
```

---

## 11. Things That Trip Up Java Devs

1. **No `++`/`--`** → use `x += 1`.
2. **Indentation is syntax**, not style — mismatched indentation = crash.
3. **`self` must be explicit** in every method — Python doesn't hide it like Java's implicit `this`.
4. **Everything is a reference** — no primitives vs objects distinction (int, str, etc. are all objects, but immutable).
5. **Mutable default args are a classic bug**:
   ```python
   def foo(items=[]):   # DON'T — shared across calls!
       items.append(1)
       return items
   ```
   Use `None` and initialize inside instead.
6. **Duck typing** — no need to implement an interface; if it has the method, it works.
7. **`__dunder__` methods** are Python's operator overloading (`__eq__`, `__str__`, `__len__`, `__add__`, etc.) — replaces `equals()`, `toString()`, `Comparable`, etc.
8. **List slicing** is powerful: `my_list[1:3]`, `my_list[::-1]` (reverse).
9. **Multiple return / unpacking**:
   ```python
   def divide(a, b):
       return a // b, a % b
   quotient, remainder = divide(10, 3)
   ```
10. **`is` vs `==`**: `is` checks identity (like Java `==` on objects), `==` checks value equality.

---

## 12. Tooling Equivalents

| Java | Python |
|---|---|
| Maven/Gradle | pip, poetry, uv |
| JUnit | pytest, unittest |
| Spring Boot | Flask, FastAPI, Django |
| Checkstyle | flake8, ruff |
| javadoc | docstrings (`"""..."""`) |
| JVM | CPython interpreter (bytecode + VM, but simpler) |
| `.jar` | no real equivalent; distribute via pip package or just scripts |

---

## Quick Practice Idea
Port a small Java class (e.g., a `BankAccount` with deposit/withdraw/balance) into Python — it'll surface most of these differences fast (constructors, encapsulation conventions, exceptions, `__str__`).
