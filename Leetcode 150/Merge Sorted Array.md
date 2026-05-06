# 88. Merge Sorted Array

## 🧠 Problem Summary

You are given two sorted arrays:

* `nums1` with size `m + n`, where first `m` elements are valid
* `nums2` with `n` elements

Goal: Merge `nums2` into `nums1` in-place as one sorted array.

---

## 🚶 Approach 1: Brute Force (Simple but Inefficient)

### Idea

* Copy all elements of `nums2` into `nums1`
* Sort the entire array

### Code

```python
for i in range(n):
    nums1[m + i] = nums2[i]

nums1.sort()
```

### Complexity

* Time: **O((m + n) log (m + n))**
* Space: **O(1)**

### ❌ Problems

* Ignores the fact that both arrays are already sorted
* Sorting again is unnecessary work
* Not optimal for large inputs

---

## 🚶‍♂️ Approach 2: Extra Array (Better but uses space)

### Idea

* Use a new array to merge both arrays like merge step in merge sort
* Copy back to `nums1`

### Code

```python
res = []
i = j = 0

while i < m and j < n:
    if nums1[i] < nums2[j]:
        res.append(nums1[i])
        i += 1
    else:
        res.append(nums2[j])
        j += 1

while i < m:
    res.append(nums1[i])
    i += 1

while j < n:
    res.append(nums2[j])
    j += 1

for i in range(m + n):
    nums1[i] = res[i]
```

### Complexity

* Time: **O(m + n)**
* Space: **O(m + n)**

### ❌ Problems

* Uses extra space (not in-place)
* Interviewers usually expect in-place solution

---

## 🚀 Approach 3: Optimal (Two Pointers from End)

### 💡 Key Insight

* Fill `nums1` from the back to avoid overwriting elements
* Compare largest elements and place them correctly

---

### Code

```python
i = m - 1
j = n - 1
k = m + n - 1

while j >= 0:
    if i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1
    k -= 1
```

---

### Complexity

* Time: **O(m + n)**
* Space: **O(1)**

---

### ✅ Why this is the best

* No sorting
* No extra space
* Uses already sorted property efficiently

---

## 🎯 Interview Strategy (How to Speak)

1. Start with brute force:

   > “We can copy and sort, but that would take O((m+n) log(m+n))…”

2. Improve:

   > “Since arrays are sorted, we can merge using extra space in O(m+n)…”

3. Optimize:

   > “To avoid extra space, we can fill from the back using two pointers…”

---

## ⚠️ Common Pitfalls

* Forgetting to check `i >= 0`
* Overwriting elements in `nums1`
* Using unnecessary sorting
* Returning array instead of modifying in-place

---

## 🔥 Final Takeaway

This problem is a classic example of:

* Two pointer technique
* Thinking **backwards to avoid overwriting**
* Using constraints smartly

---
