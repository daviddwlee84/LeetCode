# 121. Best Time to Buy and Sell Stock`

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1**:

```txt
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2**:

```txt
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solution

### Dynamic Programming

* Time complexity: O(n)
* Space complexity: O(1)

1. Only one transaction => you only need to find a minimum before a maximum
2. Go through each price
3. Update minimum as "Buy it price" if the price of ith day is lower
4. Find the maximum of the ith day price minus minimum

### Greedy

Record current minimum and keep updating the maximum difference
