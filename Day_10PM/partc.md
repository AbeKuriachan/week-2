# Python Scopes & Closures — Assignment Answers

---

## Q1 — The LEGB Rule (Conceptual)

### What is LEGB?

Python resolves every name by searching four scopes **in order**, stopping at the first match:

| Letter | Scope | Where |
|--------|-------|-------|
| **L** | Local | Inside the current function |
| **E** | Enclosing | Any outer (enclosing) function — relevant in closures/nested functions |
| **G** | Global | Module-level names |
| **B** | Built-in | Python's built-ins (`len`, `print`, `range`, …) |

---

### Concrete Example

```python
# ── B (Built-in) ─────────────────────────────────────
# len, print, range … always available

x = "global x"          # ── G (Global) ──────────────

def outer():
    x = "enclosing x"   # ── E (Enclosing) ────────────

    def inner():
        x = "local x"   # ── L (Local) ────────────────
        print(x)        # → "local x"

    inner()
    print(x)            # → "enclosing x"

outer()
print(x)                # → "global x"
```

Each `print(x)` resolves `x` by walking outward from its own scope until it finds a binding.



---

### Local vs Global — What Happens When Names Collide

```python
score = 100          # Global

def show_score():
    score = 42       # New LOCAL variable — shadows the global
    print(score)     # → 42  (local wins)

show_score()
print(score)         # → 100  (global unchanged)
```

The local `score` **shadows** the global one inside the function. The global is completely unaffected. This is usually intentional and desirable — functions should not reach out and change external state.

---

### The `global` Keyword

`global` forces Python to treat a name as the module-level variable instead of creating a local one.

```python
counter = 0

def increment():
    global counter      # "I mean the module-level counter"
    counter += 1        # mutates the global

increment()
increment()
print(counter)          # → 2
```

Without `global`, the line `counter += 1` raises `UnboundLocalError` because Python sees the assignment and treats `counter` as local, but it has no local value yet.

---

### Why `global` Is a Code Smell

1. **Hidden coupling** — the function silently depends on (and modifies) external state. Callers cannot see this from the function signature.
2. **Hard to test** — you must manage global state between test cases.
3. **Thread-unsafe** — two threads calling the function simultaneously can corrupt the shared variable.
4. **Violates "function as a black box"** — a function should transform inputs → outputs, not mutate the world.

---

### The Better Alternative — Return Values & Parameters

Instead of reaching out to mutate a global, **pass state in and return it out**:

```python
# ❌  global keyword  (code smell)
total = 0
def add(n):
    global total
    total += n

# ✅  pure function  (preferred)
def add(total, n):
    return total + n

total = 0
total = add(total, 5)
total = add(total, 3)
print(total)   # → 8
```

For mutable shared state that genuinely must persist, use a **class**:

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

c = Counter()
c.increment()
c.increment()
print(c.value)   # → 2
```

---

---

## Q2 — `memoize` Decorator (Coding)

### Implementation

```python
def memoize(func):
    """
    Decorator that caches the results of a function call.

    Uses the tuple of positional arguments as the cache key.
    On repeated calls with the same arguments, returns the
    cached result without re-executing the function.

    Args:
        func: Any callable whose return value depends only
              on its arguments (i.e., a pure function).

    Returns:
        A wrapped version of func with an attached .cache dict.
    """
    cache = {}                          # closed over by wrapper — one dict per decorated function

    def wrapper(*args):
        if args not in cache:           # cache miss → compute and store
            cache[args] = func(*args)
        return cache[args]              # cache hit  → return stored result

    wrapper.cache = cache               # expose cache for inspection / testing
    wrapper.__name__ = func.__name__    # preserve original function name
    return wrapper


# ── Usage ────────────────────────────────────────────────────────────────────

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Without memoization, fibonacci(50) requires ~2^50 recursive calls (~10^15).
# With memoization, each value from 0..50 is computed exactly once → 50 calls.

print(fibonacci(10))   # → 55
print(fibonacci(50))   # → 12586269025  (instant)

# Inspect what was cached
print(list(fibonacci.cache.items())[:5])
# [((0,), 0), ((1,), 1), ((2,), 1), ((3,), 2), ((4,), 3)]
```

---

### How It Works — Step by Step

```
fibonacci(5)
│
├─ cache miss → calls fibonacci(4) + fibonacci(3)
│   ├─ cache miss → calls fibonacci(3) + fibonacci(2)
│   │   ├─ cache miss → calls fibonacci(2) + fibonacci(1)
│   │   │   ├─ cache miss → calls fibonacci(1) + fibonacci(0)
│   │   │   │   ├─ base case → returns 1   ← stored as cache[(1,)] = 1
│   │   │   │   └─ base case → returns 0   ← stored as cache[(0,)] = 0
│   │   │   └─ returns 1                   ← stored as cache[(2,)] = 1
│   │   └─ cache HIT for (2,) → returns 1  (no recomputation)
│   │   └─ returns 2                       ← stored as cache[(3,)] = 2
│   └─ cache HIT for (3,) → returns 2
│   └─ returns 3                           ← stored as cache[(4,)] = 3
└─ cache HIT for (4,) → returns 3
└─ returns 5                               ← stored as cache[(5,)] = 5
```

Each `fibonacci(k)` is computed **exactly once**. Complexity drops from **O(2ⁿ) → O(n)**.

---

### Why Use a Tuple as Cache Key?

A dict key must be **hashable**. Tuples are hashable; lists are not.  
`args` is already a tuple when received via `*args`, so no conversion is needed.

```python
cache[(5,)]     # valid key ✅
cache[[5]]      # TypeError: unhashable type: 'list' ❌
```

---

### Standard Library Equivalent

Python ships with `functools.lru_cache` which does this (and more) out of the box:

```python
from functools import lru_cache

@lru_cache(maxsize=None)   # maxsize=None → unbounded cache (same as our memoize)
def fibonacci(n):
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

---

## Q3 — Debug & Fix (Mutable Default + Scope Bug)

### The Buggy Code

```python
total = 0

def add_to_cart(item, cart=[]):      # Bug 1: mutable default argument
    cart.append(item)
    total = total + len(cart)         # Bug 2: UnboundLocalError (scope)
    return cart
```

---

### Bug 1 — Mutable Default Argument

#### What is it?

Default argument values are evaluated **once** when the `def` statement executes, not on every call. A list is mutable, so the **same list object** is reused across every call that omits the `cart` argument.

#### What actually happens

```python
print(add_to_cart('apple'))    # → ['apple']
print(add_to_cart('banana'))   # → ['apple', 'banana']  ← WRONG!
```

The second call returns `['apple', 'banana']` because `cart` is still the list from the first call — `'apple'` was never removed.

#### The Fix — Use `None` as the sentinel

```python
def add_to_cart(item, cart=None):   # ✅ None is immutable
    if cart is None:
        cart = []                    # fresh list on every call
    cart.append(item)
    ...
```

Now each call without an explicit `cart` gets its own new list.

---

### Bug 2 — UnboundLocalError (Scope)

#### What is it?

Inside `add_to_cart`, the line:

```python
total = total + len(cart)
```

contains an **assignment** to `total`. Python sees this assignment and marks `total` as a **local variable** for the entire function body. When it then tries to read `total` on the right-hand side of `=`, the local `total` doesn't have a value yet → `UnboundLocalError`.

#### What actually happens

```
UnboundLocalError: local variable 'total' referenced before assignment
```

The function never even returns; it crashes immediately.

#### The Fix — Don't use a shared global; pass and return

```python
def add_to_cart(item, cart=None, total=0):   # ✅ total is now a parameter
    if cart is None:
        cart = []
    cart.append(item)
    total = total + len(cart)
    return cart, total
```

Or, if a running total genuinely needs to persist across calls, use a class:

```python
class ShoppingCart:
    def __init__(self):
        self.cart = []
        self.total = 0

    def add(self, item):
        self.cart.append(item)
        self.total += len(self.cart)
        return self.cart
```

---

### Fully Fixed Code

```python
def add_to_cart(item, cart=None):
    """
    Add an item to a shopping cart and return the updated cart.

    Args:
        item: The item to add.
        cart: An existing cart list. If None, a fresh list is created.

    Returns:
        The updated cart list.
    """
    if cart is None:          # Bug 1 fixed: new list on every fresh call
        cart = []

    cart.append(item)
    return cart               # Bug 2 fixed: total removed (or computed locally below)


# ── With a local total (not global) ──────────────────────────────────────────

def add_to_cart_with_total(item, cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    local_total = len(cart)   # Bug 2 fixed: purely local, no global dependency
    print(f"Cart: {cart}  |  Items in cart: {local_total}")
    return cart


print(add_to_cart_with_total('apple'))
# Cart: ['apple']  |  Items in cart: 1

print(add_to_cart_with_total('banana'))
# Cart: ['banana']  |  Items in cart: 1  ← correct: fresh cart each time
```

---

### Summary Table

| # | Bug | Root Cause | Fix |
|---|-----|-----------|-----|
| 1 | `cart=[]` default shared across calls | Mutable default evaluated once at `def` time | Use `cart=None` and create `[]` inside the function |
| 2 | `UnboundLocalError` on `total` | Assignment makes `total` local; no local value exists yet | Remove global dependency; use a local variable or parameter |