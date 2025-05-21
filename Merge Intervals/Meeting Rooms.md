# 📚 Meeting Rooms

## 📝 Problem Statement

Given an array of meeting time intervals where each interval is represented as:
[start_i, end_i] (with start_i < end_i)
Determine if a person can **attend all meetings** without any time conflicts.

---

## 📥 Example

**Input:**  
`intervals = [(0,30),(5,10),(15,20)]`  
**Output:**  
`False`

**Explanation:**  
- `(0,30)` and `(5,10)` overlap → Conflict  
- `(0,30)` and `(15,20)` overlap → Conflict  
Hence, it's **not possible** to attend all meetings.

---

## 💡 Approach

1. **Sort** the intervals by their **start time**.
2. Iterate through the sorted list:
   - For each pair of adjacent meetings, check if the **start time** of the current meeting is **less than** the **end time** of the previous meeting.
   - If so, there's a **conflict** → return `False`.
3. If no conflicts are found, return `True`.

---

## ✅ Python Code

```python
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort meetings by start time
        intervals.sort(key=lambda i: i.start)

        # Check for overlapping meetings
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True
```
⏱️ Time Complexity
O(n log n) — due to sorting the intervals, n is the number of meetings.

💾 Space Complexity
O(1) — constant extra space is used (excluding the space required for sorting, which depends on the language's sorting implementation).
