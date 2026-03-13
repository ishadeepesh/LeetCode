# ♾️ Find Position of an Element in a Sorted Array of Infinite Numbers

## 📌 Problem Statement

Given a **sorted array of infinite numbers**, the task is to find the **index of a given element `k`**.

Since the array size is theoretically **infinite**, we **cannot use the length of the array directly**.
Instead, we must determine a suitable search range before applying **Binary Search**.

If the element is **not present**, return:

```text
-1
```

---

## 🧾 Example

### Example 1

**Input**

```text
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
k = 10
```

**Output**

```text
4
```

### Explanation

The value **10** exists in the array at **index 4**.

---

### Example 2

**Input**

```text
arr = [2, 5, 7, 9]
k = 3
```

**Output**

```text
-1
```

### Explanation

The value **3** does not exist in the array.

---

# 💡 Approach

Since the array is **infinite**, we cannot directly apply Binary Search because we do not know the **upper bound**.

So the approach consists of **two phases**:

---

## 🚀 Phase 1 — Find the Search Range

We gradually **expand the search window** until the target falls within the range.

Steps:

1. Start with a small window:

```text
low = 0
high = 1
```

2. Keep doubling the `high` index until:

```text
arr[high] >= key
```

3. Each step expands the window exponentially:

```text
high = 2 * high
```

This guarantees that we eventually find a range containing the target.

---

## 🔎 Phase 2 — Apply Binary Search

Once the range `[low, high]` is found, we perform a **standard Binary Search** within that range.

Binary Search efficiently finds the target in **logarithmic time**.

---

# 🧠 Key Idea

Instead of knowing the array size beforehand, we **expand the range exponentially** until we locate a region where the target might exist.

This technique is sometimes called:

✨ **Exponential Search**

---

# 🧩 Implementation (JavaScript)

```javascript
// Binary search function to find the element 
// in a given range
function binarySearch(arr, l, r, x) {
    if (r >= l) {
        let mid = Math.floor(l + (r - l) / 2);

        if (arr[mid] === x)
            return mid;

        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);

        return binarySearch(arr, mid + 1, r, x);
    }

    return -1;
}

// Function to find the position of the key in the 
// infinite-size array (represented as an array)
function findPos(arr, key) {
    let l = 0, h = 1;

    // Expand the range until key <= arr[h]
    while (h < arr.length && arr[h] < key) {
        l = h;
        h = 2 * h;
    }

    // Adjust high if it exceeds array bounds
    if (h >= arr.length)
        h = arr.length - 1;

    // Perform binary search in the identified range
    return binarySearch(arr, l, h, key);
}

const arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170];
const k = 170;

const ans = findPos(arr, k);
console.log(ans);
```

---

# ⏱️ Time Complexity

### Range Expansion

```text
O(log n)
```

The range doubles each time.

### Binary Search

```text
O(log n)
```

Search within the discovered range.

### Total Time Complexity

```text
O(log n)
```

---

# 💾 Space Complexity

```text
O(1)
```

Only constant extra space is used.

---

# 🏁 Summary

✨ Uses **Exponential Search + Binary Search**
✨ Efficient even when the array size is unknown
✨ Expands search window exponentially
✨ Maintains **O(log n)** time complexity

This pattern appears in many problems involving **unknown or unbounded data structures**.

---
