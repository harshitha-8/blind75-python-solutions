# Blind 75 LeetCode Solutions in Python

A comprehensive collection of Python solutions to the Blind 75 LeetCode problems with detailed explanations, visualizations, and complexity analysis.

## 📊 Progress Tracker

![Progress](https://img.shields.io/badge/Solved-3%2F75-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

| Category | Solved | Total |
|----------|--------|-------|
| Array | 3 | 10 |
| Binary | 0 | 5 |
| Dynamic Programming | 0 | 11 |
| Graph | 0 | 8 |
| Interval | 0 | 5 |
| Linked List | 0 | 6 |
| Matrix | 0 | 4 |
| String | 0 | 10 |
| Tree | 0 | 14 |
| Heap | 0 | 3 |

## 🗂️ Problem Categories

### Array (3/10)

#### ✅ [Two Sum](./problems/array/two_sum) - Easy
**Problem**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to target.

**Key Concept**: Hash Map Lookup Pattern
- Use a dictionary to store numbers as you iterate
- For each number, check if its complement (target - num) exists
- **Time**: O(n) | **Space**: O(n)

**Solution Approach**:
```python
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
