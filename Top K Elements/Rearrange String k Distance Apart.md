# 🔎 Rearrange String k Distance Apart

## 🧩 Problem

Given a string `s` and an integer `k`, rearrange the string such that:

> 🔑 The same characters are at least **k distance apart**

If it is not possible, return `""`.

---

## 📌 Example

**Input**

```python
s = "aabbcc"
k = 3
```

**Output**

```text
"abcabc"
```

---

# 💡 Key Insight

> Always pick the **most frequent character**, but once used, it must **wait for k steps** before being reused.

---

# 🧠 Strategy (Greedy + Max Heap + Cooldown Queue)

1️⃣ Count frequency of characters
2️⃣ Use a **max heap** to always pick the most frequent character
3️⃣ Use a **queue (cooldown)** to store recently used characters
4️⃣ After `k` steps, reinsert characters back into heap
5️⃣ Continue until all characters are placed

---

# 💻 Python Implementation

```python
from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        char_freq = Counter(s)
        max_heap = [(-freq, char) for char, freq in char_freq.items()]
        heapify(max_heap)

        cooldown_queue = deque()
        result = []

        while max_heap:
            neg_freq, char = heappop(max_heap)
            freq = -neg_freq

            result.append(char)

            # Add to cooldown
            cooldown_queue.append((freq - 1, char))

            # Release from cooldown after k steps
            if len(cooldown_queue) >= k:
                remaining_freq, cooldown_char = cooldown_queue.popleft()
                if remaining_freq > 0:
                    heappush(max_heap, (-remaining_freq, cooldown_char))

        # If not all characters used → impossible
        if len(result) != len(s):
            return ""

        return "".join(result)
```

---

# 🔍 Example Walkthrough

```python
s = "aabbcc"
k = 3
```

### Step-by-step:

```text
Heap: [a:2, b:2, c:2]

Pick 'a' → result = "a"
Cooldown: [(1,'a')]

Pick 'b' → result = "ab"
Cooldown: [(1,'a'), (1,'b')]

Pick 'c' → result = "abc"
Cooldown: [(1,'a'), (1,'b'), (1,'c')]

Now 'a' is released → push back to heap

Continue → "abcabc"
```

---

# ⚠️ Edge Case

```python
s = "aaabc"
k = 3
```

```text
Impossible → return ""
```

---

# ⏱ Complexity

| Type     | Complexity     |
| -------- | -------------- |
| ⏱ Time   | **O(n log k)** |
| 📦 Space | **O(n)**       |

---

# ⚖️ Why this works

* Always prioritizes **highest frequency**
* Ensures **k-distance constraint** using cooldown queue
* Prevents invalid placements greedily

---

# 🔑 Final Takeaway

```text
Use max heap for greedy selection + queue to enforce cooldown (k distance)
```

---

🚀 Pattern used in:

* Task scheduling problems
* CPU scheduling / cooldown problems
* Rearrangement with constraints
