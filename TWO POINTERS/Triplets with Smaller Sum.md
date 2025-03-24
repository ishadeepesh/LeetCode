# Count of Triplets with Sum Smaller than Given Value

## Problem Statement
Given an array `arr[]` of **distinct** integers of size `n` and a value `sum`, the task is to find the **count** of triplets `(i, j, k)` such that `i < j < k` and `arr[i] + arr[j] + arr[k]` is smaller than the given `sum`.

### Example 1:
#### **Input:**
n = 5, sum = 14 arr = [2, 4, 6, 8, 9]
#### **Output:**
1
#### **Explanation:**
The only valid triplet is **(2,4,6)**.
#### **Explanation:**
The valid triplets are **(1,2,3)** and **(1,2,4)**.

---

## Solution
### **Approach**
1. **Sort the array** to apply the two-pointer technique.
2. Use a **nested loop**:
   - Fix the first element `arr[i]`.
   - Use **two pointers (`j`, `k`)** to find pairs `(arr[j], arr[k])` where `arr[i] + arr[j] + arr[k] < sum`.
   - If such a pair is found, **all elements from `j` to `k` are valid**, so increment the count by `(k - j)`.
   - Move `j` right for more possibilities.
3. **Time Complexity:** `O(n²)`

---

## Python Code
```python
class Solution:
    def countTriplets(self, n, sum, arr):
        count = 0
        arr.sort()
        
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            
            while j < k:
                triplet = arr[i] + arr[j] + arr[k]
                
                if triplet >= sum:
                    k -= 1  # Reduce the sum by moving k left
                else:
                    count += (k - j)  # Count all valid triplets at once
                    j += 1  # Move j right for more possibilities
                    
        return count
