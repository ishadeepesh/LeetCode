# 904. Fruit Into Baskets

## Problem Statement

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

- You only have **two baskets**, and each basket can only hold a **single type of fruit**.
- There is **no limit** on the amount of fruit each basket can hold.
- Starting from any tree of your choice, you must pick **exactly one fruit** from every tree (including the start tree) while moving to the **right**.
- The picked fruits must fit in one of your baskets.
- Once you reach a tree with fruit that **cannot fit** in your baskets, you must **stop**.

**Return the maximum number of fruits you can pick.**

---



## **Solution (Python)**
```python


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        l = 0
        num_sum = 0

        for r in fruits:
            if r not in d:
                d[r] = 0
            d[r] += 1

            if len(d) > 2:
                start = fruits[l]
                d[start] -= 1  
                if d[start] == 0:  
                    del d[start]  
                l += 1  

        for k, v in d.items():
            num_sum += v
            
        return num_sum

