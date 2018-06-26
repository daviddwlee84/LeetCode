# 23. Merge k Sorted Lists

## Description

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example**:

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
```

## Solution

* [Official Solution](https://leetcode.com/problems/merge-k-sorted-lists/solution/)
* (N: the total number of nodes; k: the number of linked lists)


### Naive - each time merge 2 linked list

(LeetCode: Time Limit Exceeded)

* Time Complexity: O(kN)
    * Almost every selection of node in final linked costs O(k) (k-1 times comparison)
    * There are NN nodes in the final linked list.
* Space Complexity: O(1) - No extra space used (only change the link)

### KMerge - each time merge k linked list

### Divide and Conquer

### Heap ?!