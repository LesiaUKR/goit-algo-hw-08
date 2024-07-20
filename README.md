# goit-algo-hw-08

# Homework Assignment on Heaps or Pyramids

## Task 1
### Description of the Assignment

Imagine you are given the following task in a technical interview, which you need to solve using a heap.

There are several network cables of different lengths, and they need to be joined two at a time into a single cable using connectors, in a way that will result in the lowest total cost. The cost of connecting two cables equals the sum of their lengths, and the total cost is the sum of connecting all cables.

The task is to find the order of joining the cables that minimizes the total cost.

## Optional Task 2

Given k sorted lists of integers. Your task is to merge them into a single sorted list. For this task, you should use a min heap to efficiently merge multiple sorted lists into one sorted list. Implement a function merge_k_lists that takes a list of sorted lists as input and returns a single sorted list.

### Example Expected Result:

```
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)

```
Output:

```
Sorted list: [1, 1, 2, 3, 4, 4, 5, 6]

```
## Acceptance Criteria

The code must execute and return the minimum possible total cost.