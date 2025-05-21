# 🏢 Meeting Rooms II

## 📝 Problem Statement

Given an array of meeting time intervals where each interval is represented as:
[start_i, end_i] (with start_i < end_i)
Return the **minimum number of meeting rooms** required to hold all the meetings **without any conflicts**.

---

## 📥 Example

**Input:**  
`intervals = [(0,40), (5,10), (15,20)]`  
**Output:**  
`2`

**Explanation:**  
- **Day 1**: (0,40)  
- **Day 2**: (5,10), (15,20)  
Minimum rooms (or days) required = **2**

---

## 💡 Approach

1. **Separate start and end times** of all meetings into two lists.
2. **Sort** both the `start` and `end` time lists.
3. Use two pointers `i` and `j` to simulate the meetings:
   - If a meeting starts before the previous one ends (`start[i] < end[j]`), we need a **new room** → `counter += 1`
   - Else, one meeting ends before the next starts → **reuse** a room → `counter -= 1`
4. Keep track of the **maximum number of concurrent meetings** using a variable `res`.
5. The final result is the maximum value of `counter` at any time.

---

## ✅ Python Code

```python
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Extract and sort start and end times
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = counter = 0
        i = j = 0

        # Traverse all start times
        while i < len(start):
            if start[i] < end[j]:
                counter += 1  # Need new room
                i += 1
            else:
                counter -= 1  # Free up room
                j += 1
            res = max(res, counter)

        return res
```
⏱️ Time Complexity
O(n log n) — for sorting the start and end times (dominant cost), n is the number of intervals.

💾 Space Complexity
O(n) — for storing the start and end times separately.
