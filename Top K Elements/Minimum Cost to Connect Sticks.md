# 🪵 Minimum Cost to Connect Sticks

## 🧩 Problem

You are given an array `ARR` of `N` positive integers, where each element represents the **length of a stick**.

You can **connect any two sticks**:

* Cost of connecting = `X + Y`
* New stick length = `X + Y`

🎯 **Goal:**
Connect all sticks into **one stick** with **minimum total cost**.

---

## 💡 Key Insight (Greedy Strategy)

To minimize total cost:

> 🔑 Always connect the **two smallest sticks first**

Why?

* Smaller sticks → smaller cost early
* Avoids accumulating large costs later

This is a classic **Greedy + Min Heap** problem.

---

## 🧠 Strategy

1️⃣ Convert the array into a **min heap**
2️⃣ Repeatedly:

* Take the **two smallest sticks**
* Connect them
* Add the cost
* Push the new stick back into heap
  3️⃣ Continue until only one stick remains

---

## 💻 Python Implementation

```python
import heapq

def minimumCostToConnectSticks(arr):
    heapq.heapify(arr)
    cost = 0

    while len(arr) >= 2:
        stickCost = heapq.heappop(arr) + heapq.heappop(arr)
        heapq.heappush(arr, stickCost)
        cost += stickCost

    return cost
```

---

## 📌 Example

**Input**

```python
arr = [2, 4, 3]
```

### Step-by-step:

```text
Step 1: Pick 2 and 3 → cost = 5
New heap: [4, 5]

Step 2: Pick 4 and 5 → cost = 9
New heap: [9]
```

### Total cost:

```text
5 + 9 = 14
```

**Output**

```text
14
```

---

## ⏱ Complexity Analysis

| Type     | Complexity               |
| -------- | ------------------------ |
| ⏱ Time   | **O(n log n)**           |
| 📦 Space | **O(1)** (in-place heap) |

### Why?

* Heapify → `O(n)`
* Each operation → `O(log n)`
* Total operations → `n-1`

---

## ⚠️ Edge Cases

✔ Only one stick → cost = `0`
✔ All sticks same length
✔ Large input sizes

---

## 🔑 Final Takeaway

This is similar to:

> 🧠 **Huffman Coding / Optimal Merge Pattern**

Always combine the **smallest elements first** to minimize total cost.

---

🚀 A must-know greedy + heap problem for interviews!
